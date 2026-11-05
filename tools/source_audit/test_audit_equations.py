"""Tests for tools.source_audit.equations."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.source_audit import chunk as sa_chunk
from tools.source_audit import equations


ROOT = Path(__file__).resolve().parents[2]


def _write_pages(work: Path, pages: dict[int, str]) -> None:
    for pg, body in pages.items():
        (work / f"page_{pg:04d}.md").write_text(body, encoding="utf-8")


class ScanPages(unittest.TestCase):
    def test_extracts_display_equations_in_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            _write_pages(work, {
                1: "text before $$a = b$$ more $$c = d$$",
                2: "no equations here",
                3: "$$E = mc^2$$",
            })
            recs = equations.scan_pages(work)
            self.assertEqual(len(recs), 3)
            self.assertEqual(recs[0]["page"], 1)
            self.assertEqual(recs[0]["index"], 1)
            self.assertEqual(recs[0]["latex"], "a = b")
            self.assertEqual(recs[1]["index"], 2)
            self.assertEqual(recs[2]["page"], 3)
            self.assertEqual(recs[2]["latex"], "E = mc^2")
            self.assertTrue(all(r["key"] == f"{r['page']}:{r['hash']}" for r in recs))


class FourStateStatusResolution(unittest.TestCase):
    def test_verified_beats_flagged_beats_backcheck(self):
        s, n = sa_chunk.initial_status_for_key(
            "k", {"k": {}}, {"k": {"description": "x"}}, backcheck={"k": {}}
        )
        self.assertEqual(s, "verified")
        s, n = sa_chunk.initial_status_for_key(
            "k", {}, {"k": {"description": "x"}}, backcheck={"k": {}}
        )
        self.assertEqual(s, "flagged")
        self.assertEqual(n, "x")
        s, n = sa_chunk.initial_status_for_key("k", {}, {}, backcheck={"k": {}})
        self.assertEqual(s, "backcheck")
        s, n = sa_chunk.initial_status_for_key("k", {}, {}, backcheck={})
        self.assertEqual(s, "unreviewed")

    def test_three_state_call_still_works(self):
        # callers that don't pass backcheck must continue to function
        s, n = sa_chunk.initial_status_for_key("k", {"k": {}}, {})
        self.assertEqual(s, "verified")



class FiguresStillThreeStateOnly(unittest.TestCase):
    """Regression: figures.html must not gain a backcheck filter chip."""
    def test_figures_html_has_no_backcheck_widgets(self):
        # The figures test fixture creates a manifest and renders; check the
        # rendered output for absence of backcheck.
        from tools.source_audit import audit_figures  # noqa: F401
        figures_script = Path(__file__).resolve().parent / "audit_figures.py"
        with tempfile.TemporaryDirectory() as tmp:
            tmp_p = Path(tmp)
            source = tmp_p / "BookY"
            audit = source / "audit"
            audit.mkdir(parents=True)
            manifest = {
                "schema_version": "pdf2md-assets-document/v2",
                "doc_stem": "BookY",
                "assets": [
                    {"asset_id": "BookY_p0001_fig01", "kind": "fig", "page": 1,
                     "caption": "C", "png_path": "figures/BookY_p0001_fig01.png"},
                ],
            }
            mp = source / "BookY_assets_manifest.json"
            mp.write_text(json.dumps(manifest), encoding="utf-8")
            out = audit / "figures.html"
            subprocess.run(
                [sys.executable, str(figures_script),
                 "--asset-manifest", str(mp),
                 "--audit-dir", str(audit),
                 "--output-html", str(out)],
                capture_output=True, text=True, cwd=str(ROOT),
            )
            doc = out.read_text(encoding="utf-8")
            self.assertNotIn('id="only-backcheck"', doc)
            self.assertNotIn('id="stat-backcheck"', doc)
            self.assertNotIn("katex.min.css", doc)


if __name__ == "__main__":
    unittest.main()
