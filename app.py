from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_query', methods=['POST'])
def process_query():
    data = request.get_json()
    user_query = data['queryResult']['queryText']
    # Process the user query and generate a response
    response_text = "I'm processing your request."
    return jsonify({'fulfillmentText': response_text})

if __name__ == '__main__':
    app.run(port=5000)
