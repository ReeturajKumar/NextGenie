from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional, Dict

app = FastAPI()

class QueryParameters(BaseModel):
    code: str
    programminglanguage: Optional[str] = "No language specified"

class QueryResult(BaseModel):
    parameters: QueryParameters

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/process_query")
async def process_query(request: Request):
    data = await request.json()
    parameters = data.get("queryResult", {}).get("parameters", {})
    
    # Use QueryParameters model to validate and extract parameters
    query_parameters = QueryParameters(**parameters)
    
    code = query_parameters.code
    language = query_parameters.programminglanguage

    response_text = f"Processing your {language} code snippet: {code}"
    return {"fulfillmentText": response_text}
