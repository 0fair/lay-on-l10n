from pydantic import BaseModel
from typing import List


class Book(BaseModel):
    id: int
    title: str
    author: str


class Recommendation(BaseModel):
    recommendations: List[Book]
    history: List[Book]