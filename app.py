from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_query():
    data = request.get_json()
    try:
        query_result = data.get('queryResult', {})
        query_text = query_result.get('queryText', '')
        parameters = query_result.get('parameters', {})

        code_snippet = parameters.get('code', 'No code snippet provided')
        language = parameters.get('language', 'No language specified')

        response_text = f"Processing your {language} code snippet: {code_snippet}"
        return jsonify({"fulfillmentText": response_text})

    except Exception as e:
        return jsonify({"fulfillmentText": f"Error: {str(e)}"}), 500
