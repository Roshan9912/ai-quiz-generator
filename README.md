🧠 AI Wiki Quiz Generator

DeepKlarity Technologies – Technical Assignment

📌 Objective

The AI Wiki Quiz Generator is a full-stack web application that accepts a Wikipedia article URL and automatically generates a quiz using a Large Language Model (LLM).

The system:

Scrapes Wikipedia HTML (no Wikipedia API)

Uses an LLM (Gemini free tier via LangChain) to generate quizzes

Stores results in a PostgreSQL database

Displays quizzes and history via a clean React UI

🚀 Live Demo

Frontend: 👉 https://ai-quiz-generator-ecru.vercel.app

Backend API: 👉 https://ai-quiz-generator-1-6jbj.onrender.com

API Docs: 👉 https://ai-quiz-generator-1-6jbj.onrender.com/docs

Screen Recording: 👉 https://drive.google.com/file/d/your-link/view

🛠 Tech Stack
Backend

FastAPI (Python)

PostgreSQL

SQLAlchemy ORM

BeautifulSoup (HTML scraping)

LangChain

Google Gemini (free tier)

Uvicorn

Frontend

React

Fetch API

Minimal CSS (card-based layout)


Deployment

Backend: Render

Frontend: Vercel


🧩 Application Features
🔹 TAB 1 – Generate Quiz

Input Wikipedia article URL

Scrapes article content

Generates 5–10 quiz questions

Each question includes:

Question

4 options

Correct answer

Explanation

Difficulty level

Suggests related Wikipedia topics

Stores data in PostgreSQL

Returns structured JSON response

Displays quiz in card-based UI

🔹 TAB 2 – Quiz History

Displays all previously processed Wikipedia URLs

Data fetched from PostgreSQL

Clicking Details shows full quiz in modal

Prevents duplicate re-scraping using URL-level caching

🧠 Bonus Features Implemented

✅ URL-level caching (no duplicate scraping)
✅ Graceful error handling
✅ CORS-safe frontend-backend communication
✅ Raw HTML stored in DB
✅ Fast response for repeated URLs

📂 Project Structure
ai-wiki-quiz-generator/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── scraper.py
│   │   └── llm_quiz_generator.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── api.js
│   │   └── App.js
│   └── package.json
│
├── sample_data/
│   ├── urls.txt
│   └── sample_responses.json
│
└── README.md

🔌 API Endpoints
➤ Generate Quiz
POST /generate

Request Body
{
  "url": "https://en.wikipedia.org/wiki/Machine_learning"
}

Response (Sample)
{
  "id": 1,
  "url": "https://en.wikipedia.org/wiki/Machine_learning",
  "title": "Machine learning",
  "summary": "...",
  "sections": [],
  "quiz": [...],
  "related_topics": [...]
}

➤ Quiz History
GET /history


Returns all stored quizzes from the database.

🧪 Sample Data

Located in /sample_data/

urls.txt – Tested Wikipedia URLs

sample_responses.json – Stored API outputs

🧠 LangChain Prompt Templates
Quiz Generation Prompt
You are an expert educator.

Using the following Wikipedia content, generate 5–10 quiz questions.
Each question must include:
- Question
- 4 options
- Correct answer
- Difficulty level (easy/medium/hard)
- Short explanation grounded in the content

Content:
{article_text}

Related Topics Prompt
Suggest 8–12 related Wikipedia topics based on the following article content:

{article_text}

⚙️ How to Run Locally
1️⃣ Backend Setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Create .env:

DATABASE_URL=postgresql://user:password@localhost:5432/wikiquiz
GEMINI_API_KEY=your_api_key


Run backend:

uvicorn app.main:app --reload

2️⃣ Frontend Setup
cd frontend
npm install
npm start

🧪 Testing

Test via Swagger UI: /docs

Test frontend via browser

Verified URLs:

Machine Learning

Python (programming language)

Artificial Intelligence