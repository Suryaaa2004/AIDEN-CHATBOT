from flask import Blueprint, request, jsonify
from openai_handler import ask_gpt

chat_bp = Blueprint("chat", __name__)

@chat_bp.route('/', methods=["POST"])
def chat():
    data = request.json
    answer = ask_gpt(data["question"], data["subject"])
    return jsonify({"response": answer})
