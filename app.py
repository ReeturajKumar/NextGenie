from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import google.generativeai as genai
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set your Gemini API key
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure Gemini API client
genai.configure(api_key=GEMINI_API_KEY)

# Define Pydantic models for request validation
class Parameters(BaseModel):
    code: str
    programminglanguage: str

class QueryResult(BaseModel):
    parameters: Parameters

class RequestBody(BaseModel):
    queryResult: QueryResult

class FallbackQuery(BaseModel):
    contents: list

@app.post("/process_query")
async def process_query(request_body: RequestBody):
    code = request_body.queryResult.parameters.code
    programminglanguage = request_body.queryResult.parameters.programminglanguage

    try:
        # Create a generative model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content based on the user's input
        prompt = (
            f"Generate a {programminglanguage} code snippet that performs the following task: '{code}'. "
            "The response should be formatted as a clean, well-structured code snippet."
        )
        response = model.generate_content(prompt)
        
        return {
            "generated_code": response.text.strip()
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/fallback_query")
async def fallback_query(fallback_body: FallbackQuery):
    try:
        query_text = fallback_body.contents[0]["parts"][0]["text"]

        # Create a generative model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content for the fallback query
        prompt = f"Answer the following question: {query_text}"
        response = model.generate_content(prompt)
        
        return {
            "response": response.text.strip()
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
