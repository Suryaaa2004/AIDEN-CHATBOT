# routes/goals.py
from flask import Blueprint, request, jsonify
from database import db  # <- import db from database.py

goals_bp = Blueprint('goals', __name__)

@goals_bp.route('/goals', methods=['POST'])
def add_goal():
    data = request.json
    db.goals.insert_one(data)
    return jsonify({"message": "Goal added successfully"})

@goals_bp.route('/goals', methods=['GET'])
def get_goals():
    goals = list(db.goals.find({}, {'_id': 0}))
    return jsonify(goals)
