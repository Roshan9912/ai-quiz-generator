from dotenv import load_dotenv
load_dotenv()   # 🔥 MUST BE FIRST

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from .models import Base, Quiz
from .scraper import scrape_wikipedia
from .llm_quiz_generator import generate_quiz, generate_related_topics


Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Wiki Quiz Generator")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for project/demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/generate")
def generate_quiz_api(payload: dict, db: Session = Depends(get_db)):
    url = payload.get("url")

    if not url or "wikipedia.org/wiki/" not in url:
        raise HTTPException(status_code=400, detail="Invalid Wikipedia URL")

    cached = db.query(Quiz).filter(Quiz.url == url).first()
    if cached:
        return cached

    try:
        scraped = scrape_wikipedia(url)
        MAX_CHARS = 6000  # safe for free tier

        content = scraped["content"][:MAX_CHARS]

        quiz_data = generate_quiz(content)
        topics = generate_related_topics(content)

    except Exception as e:
        error_msg = str(e)
        if "rate_limit" in error_msg or "429" in error_msg:
            raise HTTPException(
                status_code=429,
                detail="LLM rate limit reached. Please try again later or use cached quizzes."
            )
        raise HTTPException(status_code=500, detail=error_msg)


    quiz = Quiz(
        url=url,
        title=scraped["title"],
        summary=scraped["summary"],
        sections=scraped["sections"],
        key_entities=scraped["key_entities"],
        quiz=quiz_data,
        related_topics=topics,
        raw_html=scraped["raw_html"]
    )

    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    return quiz


@app.get("/history")
def quiz_history(db: Session = Depends(get_db)):
    return db.query(Quiz).all()
