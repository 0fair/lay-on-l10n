from pydantic import BaseModel
from typing import List, Optional


class Book(BaseModel):
    id: int
    title: str
    author: str

    def __init__(self, id: int, title: str, author: str) -> object:
        self.id = id
        self.title = title
        self.author = author


class Recommendation(BaseModel):
    recommendations: List[Book]
    history: List[Book]

    def __init__(self, recs: List[Book], history: List[Book]) -> object:
        self.recommendations = recs
        self.history = history



class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts_id: List[int]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts_id: Optional[List[int]] = None
