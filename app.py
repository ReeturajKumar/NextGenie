from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    req = await request.json()
    
    intent_name = req['queryResult']['intent']['displayName']
    
    if intent_name == "CodingAssistance":
        # Handle CodingAssistance intent
        return await process_query(req)
    elif intent_name == "Default Fallback Intent":
        # Handle Fallback intent
        return await fallback_query(req)
    else:
        # Handle other intents or return an error
        return {"fulfillmentText": "I am not sure how to handle this request."}

async def process_query(req):
    # Your existing logic for /process_query
    # Generate code based on the programming language and user input
    language = req['queryResult']['parameters']['programminglanguage']
    code = req['queryResult']['parameters']['code']
    # Perform code generation and return response
    return {
        "fulfillmentText": f"Here is your {language} code: ..."
    }

async def fallback_query(req):
    # Your existing logic for /fallback_query
    query_text = req['queryResult']['queryText']
    # Perform fallback response and return
    return {
        "fulfillmentText": f"Here is a response for your query: {query_text}"
    }
