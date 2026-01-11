# AI Wiki Quiz Generator

An end-to-end GenAI application that automatically generates quizzes from Wikipedia articles using a Large Language Model (LLM).

This project was built as part of an internship/assessment to demonstrate:
- Web scraping
- LLM integration via LangChain
- Backend API development using FastAPI
- Frontend UI using React
- Database persistence
- Error handling and deployment readiness

---

## 🚀 Features

### Tab 1 – Generate Quiz
- Accepts a Wikipedia article URL
- Scrapes article content using BeautifulSoup (HTML only)
- Generates 5–10 MCQs using an LLM
- Each question includes:
  - Question text
  - Four options
  - Correct answer
  - Difficulty level (easy / medium / hard)
  - Short explanation
- Extracts article sections
- Stores raw HTML, quiz data, and metadata in database
- Displays results in a clean, card-based UI

### Tab 2 – Past Quizzes (History)
- Displays all previously processed Wikipedia URLs
- Fetches data from database
- “Details” modal reuses quiz layout from Tab 1

---

## 🧠 Tech Stack

### Backend
- **Framework:** FastAPI (Python)
- **LLM:** OpenAI API via LangChain
- **Scraping:** BeautifulSoup (no Wikipedia API)
- **Database:** SQLite (PostgreSQL supported for production)
- **ORM:** SQLAlchemy

### Frontend
- **Framework:** React
- **UI:** Minimal custom UI (cards, tabs, modal)
- **API Calls:** Fetch API

---

## 🗂️ Project Structure

ai-wiki-quiz-generator/
│
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── scraper.py
│ │ ├── llm_quiz_generator.py
│ │ ├── database.py
│ │ ├── models.py
│ │ └── schemas.py
│ ├── requirements.txt
│ └── .env
│
├── frontend/
│ ├── src/
│ │ ├── api.js
│ │ ├── App.js
│ │ └── components/
│ └── package.json
│
├── sample_data/
│ ├── urls.txt
│ ├── alan_turing.json
│ ├── machine_learning.json
│ └── python.json
│
└── README.md

## ⚙️ Backend Setup (Local)

Build Command :
pip install -r requirements.txt

```bash```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload


## ⚙️ Frontend Setup (Local)

```bash```
cd frontend
npm install
npm start


🔌 API Endpoints
POST /generate

Generates a quiz from a Wikipedia URL.

```json```
{
  "url": "https://en.wikipedia.org/wiki/Alan_Turing"
}

GET /history

Returns all previously generated quizzes.


🧪 Sample Data

The sample_data/ folder contains:

urls.txt – Tested Wikipedia URLs

JSON files – Raw API outputs for:

Alan Turing

Machine Learning

Python (programming language)

This demonstrates robustness and variety in testing.


Environmental variables:

```.env```
OPENAI_API_KEY=your_openai_key (openai platform)
DATABASE_URL=sqlite:///./wikiquiz.db
