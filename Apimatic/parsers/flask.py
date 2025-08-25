from __future__ import annotations
import re
from pathlib import Path
from typing import List, Dict

from Apimatic.utils import iter_files

ROUTE = re.compile(r"@(?:\\w+)\\.route\\(([^)]+)\\)")

def parse_flask_routes(src: Path) -> List[Dict]:
    endpoints: List[Dict] = []
    for file in iter_files(src, exts=(".py",)):
        text = file.read_text(encoding="utf-8", errors="ignore")
        for m in ROUTE.finditer(text):
            path = m.group(1)
            methods = m.group(2)
            if methods:
                methods = [x.strip().strip("'\"") for x in methods.split(",")]
            else:
                methods = ["GET"]
            for method in methods:
                endpoints.append({
                    "framework": "flask",
                    "file": str(file.relative_to(src)),
                    "method": method.upper(),
                    "path": path,
                })
    return endpoints
