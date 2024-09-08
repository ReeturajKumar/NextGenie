from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class QueryResult(BaseModel):
    parameters: dict

@app.post("/process_query")
async def process_query(request: Request):
    data = await request.json()
    parameters = data.get("queryResult", {}).get("parameters", {})
    code = parameters.get("code", "")
    language = parameters.get("programminglanguage", "")

    # Ensure language and code are handled correctly
    if not language:
        language = "No language specified"

    response_text = f"Processing your {language} code snippet: {code}"
    return {"fulfillmentText": response_text}
