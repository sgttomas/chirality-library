"""Metadata stays out of publication prose while the full source is fingerprinted."""
import hashlib
import importlib.util
from pathlib import Path

import pytest

pytest.importorskip('markdown_it', reason='Manual renderer uses its separately pinned requirements')
PATH = Path(__file__).resolve().parents[2] / 'docs/alignment-manual/render_manual.py'
SPEC = importlib.util.spec_from_file_location('manual_metadata_renderer', PATH)
RENDERER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RENDERER)


def test_frontmatter_is_not_rendered_as_a_heading_or_prose(tmp_path):
    source = tmp_path / 'source.md'
    output = tmp_path / 'source.html'
    body = '# The title\n\n## The chapter\n\nKeep this body.\n'
    source.write_text(body)
    plain, _ = RENDERER.render(source, output, '2026-11-07', 'a' * 40)
    source.write_text('---\nname: invisible-header\ndescription: Metadata only.\nmetadata:\n  kind: explanation\n  surface: reference\n---\n' + body)
    typed, _ = RENDERER.render(source, output, '2026-11-07', 'b' * 40)
    def article(text):
        return text.split('<!-- BEGIN MARKDOWN CONTENT -->')[1].split('<!-- END MARKDOWN CONTENT -->')[0]
    assert article(plain) == article(typed)
    assert 'invisible-header' not in typed
    assert hashlib.sha256(source.read_bytes()).hexdigest() in typed


def test_unclosed_header_is_rejected(tmp_path):
    source = tmp_path / 'bad.md'
    source.write_text('---\nname: bad\n# Title\n\n## Chapter\n')
    with pytest.raises(ValueError, match='Unclosed document frontmatter'):
        RENDERER.render(source, tmp_path / 'bad.html', '2026-11-07', 'a' * 40)
