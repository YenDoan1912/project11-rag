import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.config import Config, load_config  # noqa: E402


def test_get_dotted_key():
    cfg = Config({"pipeline": {"mode": "rag", "rerank": False}})
    assert cfg.get("pipeline.mode") == "rag"
    assert cfg.get("pipeline.rerank") is False


def test_get_missing_returns_default():
    cfg = Config({"a": {"b": 1}})
    assert cfg.get("a.x") is None
    assert cfg.get("a.x", "fallback") == "fallback"
    assert cfg.get("khong.co.gi", 42) == 42


def test_shortcuts():
    cfg = Config({"storage": {"backend": "qdrant"}, "pipeline": {"mode": "no_rag"}})
    assert cfg.backend == "qdrant"
    assert cfg.mode == "no_rag"


def test_load_config_reads_yaml(tmp_path):
    f = tmp_path / "config.yaml"
    f.write_text("storage:\n  backend: file\npipeline:\n  mode: rag\n", encoding="utf-8")
    cfg = load_config(f)
    assert cfg.backend == "file"
    assert cfg.get("pipeline.mode") == "rag"


def test_load_config_missing_file():
    with pytest.raises(FileNotFoundError):
        load_config("khong_ton_tai_dau.yaml")


def test_load_config_rejects_non_mapping(tmp_path):
    f = tmp_path / "bad.yaml"
    f.write_text("- 1\n- 2\n", encoding="utf-8")  # list, khong phai mapping
    with pytest.raises(ValueError):
        load_config(f)
