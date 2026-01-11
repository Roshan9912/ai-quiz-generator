from sqlalchemy import Column, Integer, String, Text, JSON
from .database import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True, index=True)
    title = Column(String)
    summary = Column(Text)
    sections = Column(JSON)
    key_entities = Column(JSON)
    quiz = Column(JSON)
    related_topics = Column(JSON)
    raw_html = Column(Text)
