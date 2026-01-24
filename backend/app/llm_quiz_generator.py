import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_quiz(title: str, content: str):
    prompt = f"""
Generate 8–10 MCQ questions from the content below.
Return STRICT JSON only.

{{
  "quiz": [
    {{
      "question": "",
      "options": ["", "", "", ""],
      "answer": "",
      "difficulty": "easy|medium|hard",
      "explanation": ""
    }}
  ],
  "related_topics": []
}}

CONTENT:
{content}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)
