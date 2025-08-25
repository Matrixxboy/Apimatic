from __future__ import annotations
import re
from pathlib import Path
from typing import List, Dict

from Apimatic.utils import iter_files

# Basic urls.py pattern detection; DRF viewsets would need expansion
PATH_CALL = re.compile(r"\bpath\(['\"]([^'\"]+)['\"]\s*,")
RE_PATH_CALL = re.compile(r"\bre_path\(['\"]([^'\"]+)['\"]\s*,")

def parse_django_routes(src: Path) -> List[Dict]:
    endpoints: List[Dict] = []
    for file in iter_files(src, exts=(".py",)):
        if file.name != "urls.py":
            continue
        text = file.read_text(encoding="utf-8", errors="ignore")
        for m in PATH_CALL.finditer(text):
            endpoints.append({
                "framework": "django",
                "file": str(file.relative_to(src)),
                "method": "ANY",
                "path": "/" + m.group(1).rstrip("$"),
            })
        for m in RE_PATH_CALL.finditer(text):
            endpoints.append({
                "framework": "django",
                "file": str(file.relative_to(src)),
                "method": "ANY",
                "path": "/" + m.group(1).rstrip("$"),
            })
    return endpoints
