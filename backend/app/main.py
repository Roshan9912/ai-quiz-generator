from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


from .database import SessionLocal, engine
from .models import Base, Quiz
from .schemas import QuizRequest
from .scraper import scrape_wikipedia
from .llm_quiz_generator import generate_quiz

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Wiki Quiz Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/generate")
def generate(request: QuizRequest, db: Session = Depends(get_db)):
    try:
        # 1. Check if quiz already exists
        existing = db.query(Quiz).filter(Quiz.url == request.url).first()
        if existing:
            return {
                "id": existing.id,
                "url": existing.url,
                "title": existing.title,
                "summary": existing.summary,
                "sections": existing.sections,
                "quiz": existing.quiz,
                "related_topics": existing.related_topics,
            }

        # 2. Scrape & generate
        scraped = scrape_wikipedia(request.url)
        quiz_data, related = generate_quiz(
            scraped["clean_text"],
            scraped["title"]
        )

        record = Quiz(
            url=request.url,
            title=scraped.get("title", ""),
            summary=scraped.get("summary", ""),
            sections=scraped.get("sections", []),
            quiz=quiz_data,
            related_topics=related,
            raw_html=scraped.get("raw_html", "")
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        return {
            "id": record.id,
            "url": record.url,
            "title": record.title,
            "summary": record.summary,
            "sections": record.sections,
            "quiz": record.quiz,
            "related_topics": record.related_topics,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/history")
def history(db: Session = Depends(get_db)):
    records = db.query(Quiz).order_by(Quiz.id.desc()).all()

    return [
        {
            "id": q.id,
            "url": q.url,
            "title": q.title,
            "created_at": q.created_at
        }
        for q in records
    ]
