"""Doc config tu file YAML.

Y tuong: moi thu co the doi (backend, model, bat/tat tang) deu nam trong config.yaml,
code chi doc ra. Nhu vay thi nghiem reproducible va doi cau hinh khong phai sua code.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

DEFAULT_CONFIG_PATH = "config.yaml"


@dataclass
class Config:
    """Cau hinh da parse. Giu nguyen dang dict long nhau cho gon,
    them vai helper de lay key co dau cham cho tien."""

    data: dict[str, Any] = field(default_factory=dict)

    def get(self, dotted_key: str, default: Any = None) -> Any:
        # vd: cfg.get("pipeline.mode") -> "rag"
        node: Any = self.data
        for part in dotted_key.split("."):
            if not isinstance(node, dict) or part not in node:
                return default
            node = node[part]
        return node

    # vai shortcut hay dung
    @property
    def backend(self) -> str:
        return self.get("storage.backend", "memory")

    @property
    def mode(self) -> str:
        return self.get("pipeline.mode", "rag")


def load_config(path: str | Path = DEFAULT_CONFIG_PATH) -> Config:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Khong tim thay config: {p}")
    raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    if not isinstance(raw, dict):
        raise ValueError("Config phai la mot mapping (key: value) o cap ngoai cung")
    return Config(raw)
