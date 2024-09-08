from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_query():
    data = request.get_json()

    # Extract parameters
    query_text = data.get('queryResult', {}).get('queryText', 'No query text')
    language = data.get('queryResult', {}).get('parameters', {}).get('language', 'No language')
    code_snippet = data.get('queryResult', {}).get('parameters', {}).get('code', 'No code snippet')

    # Process the request and prepare a response
    response_text = f"Processing your {language} code snippet: {code_snippet}"

    return jsonify({
        "fulfillmentText": response_text
    })
