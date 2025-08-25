from __future__ import annotations
import re
from pathlib import Path
from typing import List, Dict

from Apimatic.utils import iter_files

ROUTE = re.compile(r"\\b(?:app|router)\\.(get|post|put|delete|patch)\\(['\"]([^'\"]+)['\"]\\)")

def parse_express_routes(src: Path) -> List[Dict]:
    endpoints: List[Dict] = []
    for file in iter_files(src, exts=(".js", ".ts")):
        text = file.read_text(encoding="utf-8", errors="ignore")
        for m in ROUTE.finditer(text):
            method = m.group(1).upper()
            path = m.group(2)
            endpoints.append({
                "framework": "express",
                "file": str(file.relative_to(src)),
                "method": method,
                "path": path,
            })
    return endpoints
