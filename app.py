import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Set your Gemini API key from environment variable
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the Gemini API client
genai.configure(api_key=GEMINI_API_KEY)

# Define Pydantic models for request validation
class Parameters(BaseModel):
    code: str
    programminglanguage: str

class QueryResult(BaseModel):
    parameters: Parameters

class RequestBody(BaseModel):
    queryResult: QueryResult

@app.post("/process_query")
async def process_query(request_body: RequestBody):
    code = request_body.queryResult.parameters.code
    programminglanguage = request_body.queryResult.parameters.programminglanguage

    try:
        # Create a generative model
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        # Generate content based on the user's input
        # Make sure to specify that you want exact code and proper formatting
        prompt = (
            f"Generate a {programminglanguage} code snippet that performs the following task: '{code}'. "
            "The response should be formatted as a clean, well-structured code snippet, similar to how it would appear in a code editor."
        )
        response = model.generate_content(prompt)
        
        # Return the generated text with proper formatting
        return {
            "generated_code": response.text.strip()  # .strip() removes any extra whitespace
        }
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
