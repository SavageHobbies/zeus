
from flask import Flask, request, jsonify
from gpt_core import GPTCore
import logging

app = Flask(__name__)
gpt = GPTCore('gpt_instructions.json')

# Configure logging
logging.basicConfig(filename='gpt_server.log', level=logging.INFO)

@app.route('/gpt', methods=['POST'])
def gpt_endpoint():
    input_data = request.json
    response = gpt.process_request(input_data['text'])
    logging.info(f"Received input: {input_data['text']}, Responded with: {response}")
    return jsonify({"response": response})

@app.route('/feedback', methods=['POST'])
def feedback_endpoint():
    feedback_data = request.json
    logging.info(f"Feedback received: {feedback_data}")
    return jsonify({"message": "Feedback received"})

if __name__ == '__main__':
    app.run(debug=True)
