import typing
from typing import Optional

import fastapi
from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import Recommendation, Book
from app.db import db_manager
import pydantic
from pydantic import BaseModel
from fastapi import FastAPI
from typing import List

recsys = fastapi.APIRouter()


@recsys.get('/recsys/{user_id}', response_model=Recommendation)
async def get_history_and_recs(user_id: int):
    history = [
        Book(1, 'Что-нибудь 1', 'Дж Роллинг 1'),
        Book(2, 'Что-нибудь 2', 'Дж Роллинг 2'),
        Book(3, 'Что-нибудь 3', 'Дж Роллинг 3'),
        Book(4, 'Что-нибудь 4', 'Дж Роллинг 4'),
        Book(5, 'Что-нибудь 5', 'Дж Роллинг 5'),
        Book(6, 'Что-нибудь 6', 'Дж Роллинг 6'),
        Book(7, 'Что-нибудь 7', 'Дж Роллинг 7'),
        Book(8, 'Что-нибудь 8', 'Дж Роллинг 8'),
        Book(9, 'Что-нибудь 9', 'Дж Роллинг 9'),
    ]

    recs = [
        Book(3, 'Что-нибудь 3', 'Дж Роллинг 3'),
        Book(1, 'Что-нибудь 1', 'Дж Роллинг 1'),
        Book(6, 'Что-нибудь 6', 'Дж Роллинг 6'),
        Book(9, 'Что-нибудь 9', 'Дж Роллинг 9'),
        Book(7, 'Что-нибудь 7', 'Дж Роллинг 7'),
    ]

    return Recommendation(history=history, recs=recs)
