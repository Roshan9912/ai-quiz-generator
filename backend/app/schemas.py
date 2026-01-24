from pydantic import BaseModel
from typing import List, Dict

class QuizRequest(BaseModel):
    url: str
