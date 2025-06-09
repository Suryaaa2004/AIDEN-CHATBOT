def format_goal_entry(goal_text):
    return {
        "goal": goal_text,
        "status": "pending"
    }

def format_flashcard(question, answer, subject):
    return {
        "question": question,
        "answer": answer,
        "subject": subject
    }
