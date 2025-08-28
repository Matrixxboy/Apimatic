from __future__ import annotations
import json
import os
from typing import Dict, List
from pathlib import Path
import google.generativeai as genai
import google.ai.generativelanguage as glm # for the API response objects

# -------- CONFIGURATION --------
API_FILE = Path.home() / ".gemini_api_key"
DEFAULT_MODEL = "gemini-1.5-flash-001"

SYSTEM_PROMPT = """
You are an expert software engineer and senior technical writer. Analyze a single API endpoint's source code and return an exhaustive documentation object.

STRICT RULES (very important):
- DO NOT speculate or invent fields. If something is not present in the code, leave it out.
- Distinguish PARAMETER KINDS correctly:
  • Path params: variables embedded in the URL path (e.g., /users/{user_id} in FastAPI, or /users/<int:user_id> in Flask). NEVER include these in "query_params".
  • Query params: only include if they are clearly read from query (e.g., FastAPI function params not in the path and/or declared with fastapi.Query; Flask usage of request.args[...] or request.args.get).
  • Request body: only include if the handler takes a Pydantic model/TypedDict/dataclass parameter OR reads request.json/request.get_json()/await request.json() etc.
- If there are NO query params, return an empty list for "query_params".
- If there is NO request body, return: "request_body": { "description": "None.", "schema": {} }.
- Keep types to: string, integer, number, boolean, object, array.
- Return ONLY a single JSON object with EXACTLY these keys: "logic_explanation", "query_params", "request_body". No markdown, no extra keys, no prose.

OUTPUT FIELDS TO PRODUCE:
1) "logic_explanation": A step-by-step explanation (4–8 lines) of the code’s control flow, purpose of variables, and any error handling/edge cases. Base this ONLY on what the code actually does.
2) "query_params": An array of objects for ALL query parameters actually used/declared.
3) "request_body": An object describing the JSON body if present.
   - If no body is used, respond with: { "description": "None.", "schema": {} }.

FRAMEWORK-SPECIFIC GUIDANCE:
- FastAPI: Path params = in route path. Query params = function params NOT in path. Request body = Pydantic model param.
- Flask: Path params = in route patterns. Query params = request.args. Request body = request.json / request.get_json().

FINAL REQUIREMENT:
- Return ONLY a single valid JSON object with keys: "logic_explanation", "query_params", "request_body".
"""

# -------- API KEY HANDLING --------
def get_api_key() -> str:
    """Retrieve stored Gemini API key, ask if missing."""
    if API_FILE.exists():
        return API_FILE.read_text().strip()
    else:
        api_key = input("Enter your Gemini API Key: ").strip()
        API_FILE.write_text(api_key)
        return api_key

def update_api_key(new_key: str) -> None:
    """Update stored API key."""
    API_FILE.write_text(new_key.strip())
    print("✅ API key updated successfully.")

# -------- MAIN FUNCTION --------
def enhance_with_gemini(endpoints: List[Dict], model_name: str = DEFAULT_MODEL) -> List[Dict]:
    """Enhances each endpoint with an AI-generated explanation using Gemini API."""
    # Use the client's built-in key management
    api_key = get_api_key()
    os.environ["GEMINI_API_KEY"] = api_key
   
    model = genai.GenerativeModel(model_name)

    for i, endpoint in enumerate(endpoints):
        source = endpoint.get("source")
        if not source:
            endpoint["ai_details"] = {
                "logic_explanation": "_No source code found to generate a description._",
                "query_params": [],
                "request_body": {},
            }
            continue

        print(f"🔍 Analyzing {endpoint.get('summary', 'endpoint')}... ({i+1}/{len(endpoints)})")

        user_prompt = f"{SYSTEM_PROMPT}\n\nHere is the API endpoint source code:\n\n{source}"

        try:
            response = model.generate_content(
                user_prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json",
                    temperature=0,
                )
            )

            api_details = json.loads(response.text)

            endpoint["ai_details"] = {
                "logic_explanation": api_details.get("logic_explanation", ""),
                "query_params": api_details.get("query_params", []),
                "request_body": api_details.get("request_body", {}),
            }

        except Exception as e:
            print(f"❌ Error analyzing {endpoint.get('summary')}: {e}")
            endpoint["ai_details"] = {
                "logic_explanation": f"_Gemini analysis failed: {e}_",
                "query_params": [],
                "request_body": {},
            }
            continue

    print("✅ AI analysis complete.")
    return endpoints