from pydantic import BaseModel
from typing import List, Dict

class QuizQA(BaseModel):
    question: str
    options: List[str]
    answer: str
    explanation: str
    difficulty: str

class QuizOutput(BaseModel):
    summary: str
    key_entities: Dict[str, List[str]]
    sections: List[str]
    quiz: List[QuizQA]
    related_topics: List[str]
