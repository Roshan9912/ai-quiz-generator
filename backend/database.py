import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import datetime

load_dotenv()
DB_URL = os.environ["DATABASE_URL"]

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Quiz(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(512))
    title = Column(String(256))
    date_generated = Column(DateTime, default=datetime.datetime.utcnow)
    scraped_content = Column(Text)
    raw_html = Column(Text, nullable=True)
    full_quiz_data = Column(Text)

def init_db():
    Base.metadata.create_all(bind=engine)
