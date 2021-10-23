from pydantic import BaseModel
from typing import List, Optional


# todo Дописать описание всех полей для автогенерации документации
class Book(BaseModel):
    id: int
    title: str
    author: str


class Recommendation(BaseModel):
    recommendations: List[Book]
    history: List[Book]


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
