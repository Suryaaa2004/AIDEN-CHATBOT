from app import db

# Define reusable database helper functions

def save_goal(goal_data):
    db.goals.insert_one(goal_data)

def get_all_goals():
    return list(db.goals.find({}, {"_id": 0}))

def save_flashcard(card_data):
    db.flashcards.insert_one(card_data)

def get_flashcards_by_subject(subject):
    return list(db.flashcards.find({"subject": subject}, {"_id": 0}))
