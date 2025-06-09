from flask import Blueprint, request, jsonify
from database import db

flashcards_bp = Blueprint("flashcards", __name__)

@flashcards_bp.route('/', methods=["GET"])
def get_flashcards():
    subject = request.args.get("subject")
    cards = list(db.flashcards.find({"subject": subject}, {"_id": 0}))
    return jsonify(cards)
