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
def generate_quiz_api(request: QuizRequest, db: Session = Depends(get_db)):

    # 1️⃣ CHECK CACHE FIRST (MOST IMPORTANT)
    existing = get_quiz_by_url(db, request.url)
    if existing:
        return existing  # 🔥 instant response, no LLM call

    # 2️⃣ SCRAPE
    scraped = scrape_wikipedia(request.url)

    # 3️⃣ LIMIT CONTENT (VERY IMPORTANT)
    MAX_CHARS = 3000
    content = scraped["content"][:MAX_CHARS]

    # 4️⃣ CALL LLM SAFELY
    try:
        quiz = generate_quiz(content)
    except Exception:
        raise HTTPException(
            status_code=429,
            detail="LLM rate limit reached. Cached quizzes still work."
        )

    # 5️⃣ SAVE TO DB
    quiz_obj = create_quiz(
        db=db,
        url=request.url,
        title=scraped["title"],
        summary=scraped["summary"],
        sections=scraped["sections"],
        key_entities=scraped.get("key_entities", {}),
        quiz=quiz,
        raw_html=scraped["raw_html"],
    )

    return quiz_obj



@app.get("/history")
def quiz_history(db: Session = Depends(get_db)):
    return db.query(Quiz).all()
