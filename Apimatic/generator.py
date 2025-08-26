from __future__ import annotations
import json
from typing import Dict, List

def generate_markdown(endpoints: List[Dict]) -> str:
    """
    Generates a Markdown string for comprehensive API documentation
    from a list of endpoint dictionaries.
    """
    # Sort by framework first for logical grouping, then by path+method
    endpoints = sorted(endpoints, key=lambda x: (x.get("framework", "other"), x.get("path", ""), x.get("method", "")))
    
    out = ["# API Documentation\n"]
    current_group = None

    for ep in endpoints:
        group = ep.get("framework", "other")
        if group != current_group:
            out.append(f"\n## {group.title()} API Endpoints\n")
            current_group = group

        title = ep.get('summary') or f"{ep.get('method','ANY')} {ep.get('path','/')}"
        out.append(f"\n### `{title}`\n")
        out.append(f"- **Endpoint:** `{ep.get('method','ANY')} {ep.get('path','/')}`\n")
        out.append(f"- **Source File:** `{ep.get('file','?')}`\n")

        description = ep.get('description', '').strip()
        if description:
            # Reformat the multi-line description for better Markdown output
            out.append(f"- **Logic Explanation:**\n")
            out.append(f"{description}\n")
        
        source = ep.get("source")
        if source:
            lang = "javascript" if ep.get("framework") == "express" else "python"
            out.append("- **Source Code:**\n")
            # Corrected the f-string syntax error here
            out.append(f'  ```{lang}\n{source.strip()}\n  ```\n')

        query_params = ep.get("query_params", [])
        out.append("- **Query Params:**\n")
        if query_params:
            out.append("  | Name | Description |\n")
            out.append("  |------|-------------|\n")
            for param in query_params:
                out.append(f"  | `{param.get('name', '')}` | {param.get('description', '')} |\n")
        else:
            out.append("  _None_\n")

        request_body = ep.get("request_body", {})
        out.append("- **Request Body:**\n")
        if request_body and (request_body.get("schema") or request_body.get("description")):
            if request_body.get("description"):
                out.append(f"  {request_body['description']}\n")
            if request_body.get("schema"):
                schema_json = json.dumps(request_body.get("schema", {}), indent=2)
                out.append(f'  ```json\n{schema_json}\n  ```\n')
        else:
            out.append("  _None_\n")

        responses = ep.get("responses", [])
        out.append("- **Responses:**\n")
        if responses:
            for resp in responses:
                out.append(f"  - **`{resp.get('status_code', '???')}`**: {resp.get('description', '')}\n")
        else:
            out.append("  _None_\n")
            
        out.append("\n")
        
    return "".join(out)