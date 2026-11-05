#!/usr/bin/env python3
"""Render a manual as deterministic, self-contained, offline HTML.

Run from any directory. See README.md for the pinned environment and invocation.
The Markdown source is trusted repository documentation; inline HTML is retained.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import hashlib
from html import escape
from html.parser import HTMLParser
from importlib.metadata import version
import os
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import quote, unquote, urlsplit

try:
    from markdown_it import MarkdownIt
except ImportError:
    raise SystemExit("Install the pinned dependencies in requirements.txt first.")


PARSER_VERSION = "4.2.0"
MDURL_VERSION = "0.1.2"
DEFAULT_SOURCE = Path(__file__).with_name("Project_Management_for_Human_Agent_Teams_Consolidated_v9.md")

CSS = """
:root {
  color-scheme: light;
  --paper: #ffffff;
  --canvas: #eeeeee;
  --ink: #111111;
  --muted: #505050;
  --line: #cccccc;
  --accent: #111111;
  --tint: #eeeeee;
  font-family: "Liberation Serif", "Times New Roman", Georgia, serif;
  font-size: 18px;
  line-height: 1.55;
}
* { box-sizing: border-box; }
html { scroll-padding-top: 2rem; }
body { margin: 0; color: var(--ink); background: var(--canvas); }
a { color: var(--accent); text-underline-offset: .17em; }
a:hover { text-decoration-thickness: .14em; }
a:focus-visible, summary:focus-visible, [tabindex]:focus-visible {
  outline: 3px solid #111111;
  outline-offset: 4px;
  border-radius: 2px;
}
.skip-link {
  position: fixed; top: .6rem; left: .6rem; z-index: 100;
  padding: .6rem 1rem; background: var(--paper); border: 2px solid var(--accent);
  transform: translateY(-200%);
}
.skip-link:focus { transform: translateY(0); }
.masthead { border-bottom: 1px solid var(--ink); background: var(--paper); }
.masthead-inner {
  max-width: 70rem; margin: auto; padding: 1.05rem 2.5rem;
  display: flex; flex-wrap: wrap; gap: .35rem 1.2rem;
  align-items: baseline; justify-content: center; text-align: center;
}
.brand { font-size: .92rem; font-weight: 700; letter-spacing: .12em; }
.masthead-label { color: var(--ink); font-size: .77rem; text-transform: uppercase; letter-spacing: .025em; }
.layout {
  max-width: 70rem; margin: auto; padding: 0 2.5rem;
  display: grid; grid-template-columns: 14rem minmax(0, 1fr); gap: 2.5rem;
}
.sidebar {
  position: sticky; top: 0; align-self: start; max-height: 100vh;
  overflow-y: auto; padding: 2rem .8rem 2rem 0;
  scrollbar-width: thin;
}
.nav-label, .eyebrow {
  margin: 0 0 .85rem; color: var(--muted); font-size: .73rem;
  font-weight: 700; text-transform: uppercase; letter-spacing: .1em;
}
.contents { list-style: none; padding: 0; margin: 0; }
.contents li { margin: .15rem 0; }
.contents a {
  display: block; padding: .34rem .65rem; border-left: 2px solid transparent;
  color: var(--muted); text-decoration: none; font-size: .86rem; line-height: 1.4;
  overflow-wrap: anywhere;
}
.contents a:hover, .contents a:focus-visible {
  color: var(--accent); background: var(--tint); border-left-color: var(--accent);
}
.nav-help { border-top: 1px solid var(--line); padding-top: 1rem; margin-top: 1.3rem; }
.nav-help p, .nav-help a { font-size: .75rem; color: var(--muted); }
.nav-help p { margin: .5rem 0; }
kbd { font: inherit; padding: .05rem .25rem; border: 1px solid var(--line); border-radius: .2rem; }
main { min-width: 0; max-width: 48.5rem; padding: 2rem 0 3rem; }
.document-meta {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: .9rem 1.5rem; margin: 0 0 1.5rem;
  font-size: .73rem; color: var(--muted);
}
.document-meta div { min-width: 0; }
.document-meta dt { font-weight: 700; letter-spacing: .025em; }
.document-meta dd { margin: .15rem 0 0; overflow-wrap: anywhere; }
.document-meta code { font-size: .9em; background: none; padding: 0; }
.fingerprint { grid-column: 1 / -1; }
.paper {
  min-width: 0; padding: 3.4rem 3rem 3rem;
  background: var(--paper); border: 1px solid var(--line);
  box-shadow: 0 2px 10px rgb(0 0 0 / .04);
}
article { max-width: 68ch; margin: auto; overflow-wrap: anywhere; }
article > :first-child { margin-top: 0; }
h1, h2, h3, h4, h5, h6 { color: #000000; line-height: 1.22; text-wrap: balance; scroll-margin-top: 2rem; }
h1 {
  max-width: 19ch; margin: 0 auto 1.65rem; font-size: clamp(2.05rem, 3.8vw, 2.8rem);
  text-align: center; text-transform: uppercase; letter-spacing: .015em;
}
article > h1 + p { margin-bottom: 2.4rem; text-align: center; font-size: .82rem; line-height: 1.45; }
h2 { font-size: 1.5rem; margin: 3.4rem 0 1.1rem; }
h3 { font-size: 1.13rem; margin: 2rem 0 .7rem; }
h4, h5, h6 { font-size: 1.02rem; margin: 1.65rem 0 .6rem; }
p { margin: 0 0 .78rem; }
article p { text-align: justify; text-justify: inter-word; hyphens: auto; }
ul, ol { padding-left: 1.5rem; }
li { padding-left: .2rem; margin: .35rem 0; }
li > p { margin: .6rem 0; }
hr { max-width: 75%; border: 0; border-top: 1px solid var(--ink); margin: 2.5rem auto; }
blockquote {
  margin: 1.4rem 1.25rem; padding: 0; background: none; border: 0;
}
blockquote > :last-child { margin-bottom: 0; }
code, pre { font-family: "Liberation Mono", "SFMono-Regular", Consolas, monospace; font-size: .83em; hyphens: none; }
code { background: #f1f1f1; padding: .08em .2em; overflow-wrap: anywhere; }
pre {
  max-width: 100%; overflow-x: auto; padding: 1rem 1.15rem; margin: 1.4rem 0;
  color: #111111; background: #f6f6f6; border: 1px solid var(--line);
  line-height: 1.5; tab-size: 4;
}
pre code { background: none; padding: 0; border-radius: 0; font-size: 1em; overflow-wrap: normal; }
.table-scroll { max-width: 100%; overflow-x: auto; margin: 1.5rem 0; }
table { width: 100%; min-width: 30rem; border-collapse: collapse; font-size: .87rem; line-height: 1.4; }
th, td { padding: .65rem .75rem; text-align: left; vertical-align: top; border: 1px solid #b8b8b8; }
th { color: #000000; background: #eeeeee; font-weight: 700; }
tbody tr { background: #ffffff; }
img, svg { max-width: 100%; height: auto; }
a[id], a[name] { scroll-margin-top: 2rem; }
p:has(> a[id]:only-child):empty { margin: 0; }
p:has(> a[id]:only-child) { margin: 0; }
h2:target, h3:target, h4:target { text-decoration: underline; text-decoration-color: #777777; text-decoration-thickness: .08em; text-underline-offset: .2em; }
.mobile-toc { display: none; }
.document-footer { margin-top: 1.5rem; color: var(--muted); font-size: .73rem; }
.document-footer p { margin: .4rem 0; }
@media (max-width: 65rem) {
  .layout { padding: 0 1.5rem; grid-template-columns: 12.5rem minmax(0, 1fr); gap: 1.5rem; }
  .masthead-inner { padding: 1rem 1.5rem; }
  .paper { padding: 2.6rem 2rem; }
}
@media (max-width: 54rem) {
  html { scroll-padding-top: 4.5rem; }
  .layout { display: block; padding: 0 1rem; }
  .sidebar { display: none; }
  .masthead-inner { padding: .85rem 1rem; gap: .2rem 1rem; }
  .mobile-toc {
    display: block; position: sticky; top: 0; z-index: 10;
    background: var(--paper); border-bottom: 1px solid var(--line);
  }
  .mobile-toc summary { padding: .75rem 1rem; cursor: pointer; color: var(--accent); font-weight: 700; font-size: .85rem; }
  .mobile-toc nav { max-height: 65vh; overflow-y: auto; padding: 0 .5rem 1rem; }
  .mobile-toc .contents a { padding: .55rem; }
  main { padding-top: 1.25rem; }
  .paper { padding: 2.2rem 1.4rem; }
  article p { text-align: left; }
  article > h1 + p { text-align: center; }
  h2, h3, h4, h5, h6, a[id], a[name] { scroll-margin-top: 4.5rem; }
  h2 { margin-top: 2.7rem; font-size: 1.4rem; }
  .document-meta { gap: .75rem 1rem; }
}
@media (max-width: 25rem) {
  :root { font-size: 17px; }
  .layout { padding: 0 .5rem; }
  .paper { padding: 1.4rem 1rem; }
  .document-meta { padding: 0 .5rem; }
}
@media print {
  @page { size: 6.75in 9.25in; margin: .68in .65in .67in .72in; }
  :root { font-size: 10.5pt; line-height: 1.2; color-scheme: light; }
  body, .paper { color: #111; background: white; }
  .masthead, .sidebar, .mobile-toc, .skip-link, .back-top { display: none; }
  .layout { display: block; max-width: none; padding: 0; }
  main { max-width: none; padding: 0; }
  .paper { padding: 0; border: 0; border-radius: 0; box-shadow: none; }
  article { max-width: none; }
  article p { margin-bottom: 4.6pt; text-align: justify; }
  .document-meta { padding: 0 0 1rem; margin-bottom: 1.5rem; border-bottom: 1px solid #bbb; }
  h1 { font-size: 26pt; }
  h2 { font-size: 18pt; margin-top: 1.8rem; }
  h3 { font-size: 12pt; }
  h4, h5, h6 { font-size: 11pt; }
  h1, h2, h3, h4, h5, h6 { break-after: avoid; }
  p, li { orphans: 3; widows: 3; }
  a { color: inherit; text-decoration: underline; }
  .table-scroll { overflow: visible; border: 0; }
  table { min-width: 0; table-layout: auto; font-size: 9pt; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; }
  th, td { padding: .45rem; }
  pre { overflow: visible; white-space: pre-wrap; overflow-wrap: anywhere; border-color: #bbb; font-size: 8pt; line-height: 1.3; }
  pre code { white-space: pre-wrap; overflow-wrap: anywhere; }
  blockquote { break-inside: avoid; background: white; }
  .document-footer { border-top: 1px solid #bbb; padding-top: .75rem; }
}
"""


class HTMLAudit(HTMLParser):
    """Collect visible text, targets, and links without rewriting source HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text: list[str] = []
        self.ids: list[str] = []
        self.fragments: list[str] = []
        self.resources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "a" and values.get("name") and values.get("name") != values.get("id"):
            self.ids.append(values["name"])
        if tag == "a" and (values.get("href") or "").startswith("#"):
            self.fragments.append(unquote(values["href"][1:]))
        if tag == "img":
            self.text.append(values.get("alt") or "")
        for attr in ("src", "srcset", "poster"):
            value = values.get(attr)
            if value and not value.startswith("data:"):
                self.resources.append(f"{tag}[{attr}]={value}")
        if tag == "link" and values.get("href"):
            self.resources.append(f"link[href]={values['href']}")

    def handle_data(self, data: str) -> None:
        self.text.append(data)


class SourceHTMLAudit(HTMLParser):
    """Accept passive document markup, not arbitrary embedded applications.

    This is an authoring constraint for trusted documentation, not a general
    HTML sanitizer. Unsupported source markup fails rather than being removed.
    Only raw HTML tokens pass here; parser-generated table alignment is safe.
    """

    tags = set("a abbr address article aside b bdi bdo blockquote br caption cite code col colgroup dd del details dfn div dl dt em figcaption figure footer h1 h2 h3 h4 h5 h6 header hr i kbd li main mark nav ol p pre q s samp section small span strong sub summary sup table tbody td th thead tr u ul var".split())
    attributes = set("id name href title class lang dir align colspan rowspan scope start reversed type value open role tabindex".split())

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in self.tags:
            self.errors.append(f"unsupported <{tag}> tag")
        for key, value in attrs:
            if key not in self.attributes and not key.startswith("aria-"):
                self.errors.append(f"unsupported {tag}[{key}] attribute")
            if key == "href" and (tag != "a" or urlsplit(value or "").scheme.lower() not in {"", "http", "https", "mailto", "tel"}):
                self.errors.append(f"unsupported {tag}[href] target")


def validate_source_html(tokens) -> None:
    audit = SourceHTMLAudit()

    def visit(items):
        for token in items:
            if token.type in {"html_block", "html_inline"}:
                audit.feed(token.content)
            if token.children:
                visit(token.children)

    visit(tokens)
    audit.close()
    if audit.errors:
        raise ValueError("Unsupported source HTML: " + "; ".join(sorted(set(audit.errors))))


def plain_text(fragment: str) -> str:
    parser = HTMLAudit()
    parser.feed(fragment)
    return "".join(parser.text).strip()


def slugify(text: str) -> str:
    """Stable lowercase heading IDs; explicit source anchors remain untouched."""
    text = unicodedata.normalize("NFC", text).lower()
    text = "".join(c for c in text if c in "_-" or c.isspace() or unicodedata.category(c)[0] in "LN")
    return re.sub(r"\s", "-", text.strip()) or "section"


def render(
    source: Path, output: Path, basis_date: str, basis_revision: str, *,
    edition_label: str = "Management manual", metadata_at_end: bool = False,
) -> tuple[str, dict]:
    if not edition_label.strip():
        raise ValueError("The edition label must not be empty.")
    for package, required in (("markdown-it-py", PARSER_VERSION), ("mdurl", MDURL_VERSION)):
        actual = version(package)
        if actual != required:
            raise ValueError(f"{package} {actual} is installed; requirements.txt pins {required}.")
    source_bytes = source.read_bytes()
    markdown = source_bytes.decode("utf-8")
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    md = MarkdownIt("commonmark", {"html": True}).enable(["table", "strikethrough"])
    tokens = md.parse(markdown)
    validate_source_html(tokens)
    source_audit = HTMLAudit()
    source_audit.feed(md.renderer.render(tokens, md.options, {}))
    reserved = {"manual-top", "manual-content"}
    collisions = reserved.intersection(source_audit.ids)
    if collisions:
        raise ValueError(f"Source anchors use reserved page IDs: {sorted(collisions)}")
    used = reserved.union(source_audit.ids)
    chapters: list[tuple[str, str]] = []
    title = ""
    title_id = ""
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        inline = tokens[index + 1]
        label = plain_text(md.renderer.renderInline(inline.children or [], md.options, {}))
        base = slugify(label)
        anchor = base
        suffix = 1
        while anchor in used:
            anchor = f"{base}-{suffix}"
            suffix += 1
        used.add(anchor)
        token.attrSet("id", anchor)
        if token.tag == "h1" and not title:
            title, title_id = label, anchor
        if token.tag == "h2":
            chapters.append((anchor, label))
    if not title or not chapters:
        raise ValueError("The manual must contain an H1 title and H2 chapters.")

    def table_open(renderer, table_tokens, index, options, env):
        env["table_number"] = env.get("table_number", 0) + 1
        return (f'<div class="table-scroll" role="region" tabindex="0" '
                f'aria-label="Table {env["table_number"]}; scroll horizontally if needed">\n'
                + renderer.renderToken(table_tokens, index, options, env))

    def table_close(renderer, table_tokens, index, options, env):
        return renderer.renderToken(table_tokens, index, options, env) + "</div>\n"

    md.add_render_rule("table_open", table_open)
    md.add_render_rule("table_close", table_close)
    body = md.renderer.render(tokens, md.options, {})
    toc = "\n".join(f'<li><a href="#{escape(anchor, quote=True)}">{escape(label)}</a></li>' for anchor, label in chapters)
    source_href = quote(Path(os.path.relpath(source, output.parent)).as_posix(), safe="/.")
    source_date = date.fromisoformat(basis_date)
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    readable_date = f"{source_date.day} {months[source_date.month - 1]} {source_date.year}"
    title_escaped = escape(title)
    metadata = f"""  <dl class="document-meta">
    <div><dt>Source basis dated</dt><dd>{readable_date}</dd></div>
    <div><dt>Repository basis</dt><dd><code>{basis_revision}</code></dd></div>
    <div class="fingerprint"><dt>Markdown source · SHA-256</dt><dd><a href="{source_href}">{escape(source.name)}</a><br><code>{source_sha}</code></dd></div>
  </dl>
"""
    metadata_before = "" if metadata_at_end else metadata
    metadata_after = metadata if metadata_at_end else ""
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="generator" content="render_manual.py; markdown-it-py {PARSER_VERSION}">
<meta name="source-sha256" content="{source_sha}">
<meta name="source-basis-date" content="{basis_date}">
<meta name="source-basis-revision" content="{basis_revision}">
<title>{title_escaped} · Chirality</title>
<style>{CSS}</style>
</head>
<body id="manual-top">
<a class="skip-link" href="#manual-content">Skip to manual</a>
<header class="masthead">
  <div class="masthead-inner"><span class="brand">CHIRALITY</span><span class="masthead-label">{escape(edition_label)} · offline reading edition</span></div>
</header>
<details class="mobile-toc">
  <summary>Contents · {len(chapters)} sections</summary>
  <nav aria-label="Sections on small screens"><ol class="contents">{toc}</ol></nav>
</details>
<div class="layout">
<aside class="sidebar">
  <nav aria-label="Sections">
    <p class="nav-label">In this manual</p>
    <ol class="contents">{toc}</ol>
  </nav>
  <div class="nav-help">
    <p>Find a term with <kbd>⌘ F</kbd> or <kbd>Ctrl F</kbd>. Use your browser’s print command for a paper copy.</p>
    <p><a href="{source_href}">Markdown source</a> · <a href="#manual-top">Back to start ↑</a></p>
  </div>
</aside>
<main id="manual-content" tabindex="-1">
{metadata_before}  <div class="paper">
    <article aria-labelledby="{escape(title_id, quote=True)}">
<!-- BEGIN MARKDOWN CONTENT -->
{body}<!-- END MARKDOWN CONTENT -->
    </article>
  </div>
  <footer class="document-footer">
{metadata_after}    <p>Complete rendering of the linked Markdown source. Document content and source links are preserved. This file needs no network connection to read.</p>
    <p>Generated with markdown-it-py {PARSER_VERSION}. The source basis above identifies this edition; consult current project records before acting.</p>
    <p class="back-top"><a href="#manual-top">Back to start ↑</a></p>
  </footer>
</main>
</div>
<script>
const mobileContents = document.querySelector('.mobile-toc');
mobileContents.addEventListener('click', (event) => {{
  if (event.target.closest('a[href^="#"]')) mobileContents.open = false;
}});
</script>
</body>
</html>
"""
    audit = HTMLAudit()
    audit.feed(html)
    duplicates = sorted(key for key, count in Counter(audit.ids).items() if count > 1)
    missing = sorted(set(audit.fragments).difference(audit.ids).difference({""}))
    if duplicates or missing or audit.resources:
        raise ValueError(f"HTML validation failed: duplicate IDs={duplicates}; missing anchors={missing}; non-embedded assets={audit.resources}")
    return html, {
        "source": str(source), "output": str(output), "source_sha256": source_sha,
        "output_sha256": hashlib.sha256(html.encode("utf-8")).hexdigest(),
        "chapters": len(chapters), "headings": sum(t.type == "heading_open" for t in tokens),
        "tables": sum(t.type == "table_open" for t in tokens),
        "code_blocks": sum(t.type in {"fence", "code_block"} for t in tokens),
        "parser": f"markdown-it-py {PARSER_VERSION}",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, help="Defaults to the source path with an .html extension")
    parser.add_argument("--basis-date", required=True, help="Source basis date, YYYY-MM-DD (never inferred from the clock)")
    parser.add_argument("--basis-revision", required=True, help="Full repository basis commit SHA (never inferred from HEAD)")
    parser.add_argument("--edition-label", default="Management manual", help="Reading-edition label shown in the masthead")
    parser.add_argument("--metadata-at-end", action="store_true", help="Place visible source metadata after the document")
    parser.add_argument("--check", action="store_true", help="Fail if the existing HTML differs; do not write")
    args = parser.parse_args()
    try:
        date.fromisoformat(args.basis_date)
        if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", args.basis_revision):
            raise ValueError("--basis-revision must be a full lowercase commit SHA.")
        source = args.source.resolve()
        output = (args.output or source.with_suffix(".html")).resolve()
        if source == output:
            raise ValueError("The HTML output cannot overwrite the Markdown source.")
        html, summary = render(
            source, output, args.basis_date, args.basis_revision,
            edition_label=args.edition_label, metadata_at_end=args.metadata_at_end,
        )
        if args.check:
            if not output.exists() or output.read_bytes() != html.encode("utf-8"):
                raise ValueError(f"{output} is missing or stale; rerun without --check.")
            action = "Verified"
        else:
            output.write_text(html, encoding="utf-8", newline="\n")
            action = "Rendered"
    except (ValueError, OSError) as error:
        parser.exit(1, f"Error: {error}\n")
    print(f"{action} {summary['output']}")
    print(f"{summary['chapters']} sections; {summary['headings']} headings; {summary['tables']} tables; {summary['code_blocks']} code blocks")
    print(f"Source SHA-256: {summary['source_sha256']}")
    print(f"HTML SHA-256:   {summary['output_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
