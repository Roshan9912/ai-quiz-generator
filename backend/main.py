from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, Quiz, init_db
from scraper import scrape_wikipedia
from llm_quiz_generator import generate_quiz_with_llm
import json

init_db()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://reimagined-goldfish-7vpq45p4rqp6fxwwr-5173.app.github.dev",  # Your frontend URL!
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/generate_quiz")
def generate_quiz(payload: dict):
    url = payload["url"]
    soup = scrape_wikipedia(url)
    quizdata = generate_quiz_with_llm(soup["title"], soup["clean_text"], soup["sections"])
    db = SessionLocal()
    q = Quiz(
        url=url,
        title=soup["title"],
        scraped_content=soup["clean_text"],
        raw_html=soup["raw_html"],
        full_quiz_data=json.dumps(quizdata)
    )
    db.add(q)
    db.commit()
    db.refresh(q)
    db.close()
    return quizdata

@app.get("/history")
def history():
    db = SessionLocal()
    records = db.query(Quiz).order_by(Quiz.id.desc()).all()
    db.close()
    return [
        {"id": q.id, "url": q.url, "title": q.title, "date_generated": q.date_generated.isoformat()}
        for q in records
    ]

@app.get("/quiz/{quiz_id}")
def get_quiz(quiz_id: int):
    db = SessionLocal()
    record = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    db.close()
    if not record:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return json.loads(record.full_quiz_data)
