from sqlalchemy.orm import Session
from .models import Quiz

def get_quiz_by_url(db: Session, url: str):
    return db.query(Quiz).filter(Quiz.url == url).first()

def create_quiz(db: Session, data: dict):
    quiz = Quiz(**data)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz

def get_all_quizzes(db: Session):
    return db.query(Quiz).order_by(Quiz.id.desc()).all()

def get_quiz_by_id(db: Session, quiz_id: int):
    return db.query(Quiz).filter(Quiz.id == quiz_id).first()
