from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_msg = data.get('message', '')

    # Example simple logic (replace with OpenAI/chatbot logic later)
    if user_msg.strip().lower() == 'hi':
        reply = "Hello! How can I assist you today?"
    elif '+' in user_msg or '-' in user_msg or '*' in user_msg or '/' in user_msg:
        try:
            result = eval(user_msg)
            reply = f"Result: {result}"
        except:
            reply = "Sorry, I couldn't compute that."
    else:
        reply = f"I heard you say: {user_msg}"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True,port=5000)
