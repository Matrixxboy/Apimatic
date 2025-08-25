from __future__ import annotations
from typing import Dict, List


def generate_markdown(endpoints: List[Dict]) -> str:
    # Sort by path+method for consistency
    endpoints = sorted(endpoints, key=lambda x: (x.get("path",""), x.get("method","")))
    out = ["# API Documentation\n"]
    current_group = None
    for ep in endpoints:
        group = ep.get("framework", "other")
        if group != current_group:
            out.append(f"\n## {group.title()}\n")
            current_group = group
        title = ep.get('summary') or f"{ep.get('method','ANY')} {ep.get('path','/')}"
        out.append(f"### {title}\n")
        out.append(f"- **Endpoint:** `{ep.get('method','ANY')} {ep.get('path','/')}`\n")
        out.append(f"- **Source:** `{ep.get('file','?')}`\n")
        out.append(f"- **Description:** {ep.get('description','_add description_')}\n")
        out.append("- **Query Params:** _add params_\n")
        out.append("- **Request Body:** _add schema_\n")
        out.append("- **Responses:** _add examples_\n\n")
    return "\n".join(out)
