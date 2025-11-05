<<<<<<< HEAD
=======
# ai-quiz-generator
>>>>>>> 476284b78047cee85dab86104affc56c4bfd5828
AI Wikipedia Quiz Generator
Overview
This project is a full-stack application that scrapes any Wikipedia article and uses an LLM (Google Gemini via LangChain) to generate high-quality quiz questions including answers, explanations, difficulty ratings, and related topics. The app includes both a FastAPI backend and a React frontend, with persistent quiz history and sample data for demonstration.

Technologies Used
Backend: FastAPI (Python), SQLAlchemy ORM, BeautifulSoup (scraping), LangChain (LLM + Gemini API)

Frontend: React + Vite, Tailwind CSS

Database: SQLite (local) or MySQL/PostgreSQL (production)

Other: Codespaces, CORS middleware, RESTful APIs

Setup & Run Instructions
Backend:

cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Add API keys to .env, e.g. GEMINI_API_KEY
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Frontend:

cd frontend
npm install
npm run dev
Note: In Codespaces, use the provided preview URLs for both frontend (5173) and backend (8000).
Backend must be running with proper CORS config for frontend to connect.

Application Features
Input: User enters any valid Wikipedia article URL
Ex:
https://en.wikipedia.org/wiki/Alan_Turing

https://en.wikipedia.org/wiki/Python_(programming_language)

https://en.wikipedia.org/wiki/Machine_learning

Quiz Generator: Scrapes article, sends content to LLM, receives quiz JSON

Quiz Format: Each question has 4 options, a correct answer, explanation, difficulty level, and related topics

History: Quiz history saved and viewable, with modal for quiz details and full explanations

Sample Data: See sample_data/

Error Handling: Includes validation for Wikipedia URLs and shows frontend/backend errors

LangChain Prompt Template
Paste your prompt here (example):

text
You are an AI tutor. Given the Wikipedia article "{title}", create 5 multiple-choice questions. For each, provide 4 answer options, identify the correct answer, offer a one-sentence explanation, and indicate the question's difficulty (easy/medium/hard). Return as valid JSON:

{
  "summary": "...",
  "quiz": [
    {
      "text": "...",
      "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
      "correct_answer": "B",
      "explanation": "...",
      "difficulty_level": "easy"
    }
    // more questions ...
  ],
  "key_entities": [...],
  "sections": [...],
  "related_topics": [...]
}
Sample Data
See the sample_data/ folder for example Wikipedia articles and their generated quiz JSON:

alan_turing.json

python.json

machine_learning.json


Troubleshooting
CORS errors: Ensure backend CORS settings match your frontend URL exactly and restart backend after changes.

Frontend can't connect: Check backend runs on --host 0.0.0.0 and API URLs are correct.

Quiz not generated: Double-check API keys and environment variables. Review backend logs for errors.

Contact
<<<<<<< HEAD
For help or questions, contact: [kokkularamana225@gmail.com]
=======
For help or questions, contact: [kokkularamana225@gmail.com]
>>>>>>> 476284b78047cee85dab86104affc56c4bfd5828
