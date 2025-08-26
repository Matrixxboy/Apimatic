from __future__ import annotations
import re
from pathlib import Path
from typing import List, Dict

from Apimatic.utils import iter_files

ROUTE_RE = re.compile(
    r"""
    \b(?:app|router)\.
    (get|post|put|delete|patch)
    \s*\(\s*
    ['"`]([^'"`]+)['"`]
    \s*,\s*
    (
        (?:async\s*)?
        \([^)]*\)
        \s*=>\s*
        \{[\s\S]*?\}
    )
    """,
    re.VERBOSE | re.MULTILINE
)

def parse_express_routes(src: Path) -> List[Dict]:
    endpoints: List[Dict] = []
    for file in iter_files(src, exts=(".js", ".ts")):
        try:
            text = file.read_text(encoding="utf-8", errors="ignore")
            for match in ROUTE_RE.finditer(text):
                end_index = match.end(0)
                if text[end_index:].lstrip().startswith(')'):
                    method, path, source = match.groups()
                    endpoints.append({
                        "framework": "express",
                        "file": str(file.relative_to(src)),
                        "method": method.upper(),
                        "path": path,
                        "source": source.strip(),
                        "summary": f"{method.upper()} {path}"
                    })
        except Exception:
            continue
            
    return endpoints
