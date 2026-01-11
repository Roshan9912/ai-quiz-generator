from pydantic import BaseModel
from typing import List, Dict

class QuizRequest(BaseModel):
    url: str

class QuizResponse(BaseModel):
    id: int
    url: str
    title: str
    summary: str
    sections: List[str]
    key_entities: Dict
    quiz: List[Dict]
    related_topics: List[str]
