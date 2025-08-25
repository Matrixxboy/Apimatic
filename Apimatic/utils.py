from __future__ import annotations
from pathlib import Path
from typing import Iterable, Tuple


def iter_files(root: Path, exts: Tuple[str, ...]) -> Iterable[Path]:
    root = Path(root)
    for p in root.rglob("*"):
        if p.is_file() and p.suffix in exts:
            yield p
