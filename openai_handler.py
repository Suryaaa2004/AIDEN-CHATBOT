import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def ask_gpt(question, subject):
    prompt = f"You are a study assistant for {subject}. Answer this question:\n{question}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
