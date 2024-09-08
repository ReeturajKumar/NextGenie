from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_query():
    data = request.get_json()
    query_result = data.get('queryResult', {})
    code_snippet = query_result.get('parameters', {}).get('code', 'No code snippet provided')
    language = query_result.get('parameters', {}).get('language', 'No language specified')

    response_text = f"Processing your {language} code snippet: {code_snippet}"
    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(debug=True)
