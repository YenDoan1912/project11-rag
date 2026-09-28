import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.models import Document  # noqa: E402


def test_is_labeled():
    assert Document("d1", "x", label="benign").is_labeled
    assert not Document("d2", "x").is_labeled


def test_preview_shortens_long_text():
    long_text = "import os\n" + "x = 1  " * 50
    p = Document("d", long_text).preview(n=20)
    assert len(p) <= 20
    assert "\n" not in p


def test_preview_keeps_short_text():
    assert Document("d", "eval(x)").preview() == "eval(x)"
