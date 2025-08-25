from __future__ import annotations
import json
import subprocess
from typing import Dict, List, Tuple

SYSTEM_PROMPT = (
    "You are an expert technical writer. Given raw endpoint data (method, path, framework, file), "
    "return an enriched JSON array of endpoints. For each endpoint, add 'summary' and 'description'. "
    "If information is missing, make a sensible, concise placeholder. IMPORTANT: Return ONLY JSON."
)


def _key(ep: Dict) -> Tuple[str, str]:
    return (str(ep.get("method", "")).upper(), str(ep.get("path", "")))


def _merge(original: List[Dict], enriched: List[Dict]) -> List[Dict]:
    base = { _key(ep): ep for ep in original }
    for e in enriched:
        k = _key(e)
        if k in base:
            # Merge summary/description into the original dict, preserve framework/file
            if e.get("summary"):
                base[k]["summary"] = e["summary"]
            if e.get("description"):
                base[k]["description"] = e["description"]
    return list(base.values())


def enhance_with_ollama(endpoints: List[Dict], model: str = "llama3:instruct") -> List[Dict]:
    payload = {
        "system": SYSTEM_PROMPT,
        "user": {
            "task": "enrich_endpoints",
            "endpoints": [
                {"method": ep.get("method"), "path": ep.get("path"), "framework": ep.get("framework"), "file": ep.get("file")}
                for ep in endpoints
            ],
        },
    }
    prompt = json.dumps(payload, ensure_ascii=False)

    try:
        proc = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            capture_output=True,
            check=False,
        )
        text = (proc.stdout or b"").decode("utf-8", errors="ignore").strip()
    except FileNotFoundError:
        # ollama not installed; return original
        return endpoints

    # Extract first JSON array from output
    start = text.find("[")
    end = text.rfind("]")
    if start == -1 or end == -1 or end <= start:
        return endpoints

    try:
        enriched = json.loads(text[start:end+1])
        if isinstance(enriched, list):
            return _merge(endpoints, enriched)
    except Exception:
        pass
    return endpoints
