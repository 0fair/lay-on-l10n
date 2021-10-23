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
        {"id": 1, "title": "Как-нибудь 1", "author": "Дж Роллинг 1"},
        {"id": 2, "title": "Как-нибудь 2", "author": "Дж Роллинг 2"},
        {"id": 3, "title": "Как-нибудь 3", "author": "Дж Роллинг 3"},
        {"id": 4, "title": "Как-нибудь 4", "author": "Дж Роллинг 4"},
        {"id": 5, "title": "Как-нибудь 5", "author": "Дж Роллинг 5"},
        {"id": 6, "title": "Как-нибудь 6", "author": "Дж Роллинг 6"},
        {"id": 7, "title": "Как-нибудь 7", "author": "Дж Роллинг 7"},
        {"id": 8, "title": "Как-нибудь 8", "author": "Дж Роллинг 8"},
        {"id": 9, "title": "Как-нибудь 9", "author": "Дж Роллинг 9"},
    ]

    recs = [
        {"id": 3, "title": "Как-нибудь 3", "author": "Дж Роллинг 3"},
        {"id": 1, "title": "Как-нибудь 1", "author": "Дж Роллинг 1"},
        {"id": 6, "title": "Как-нибудь 6", "author": "Дж Роллинг 6"},
        {"id": 9, "title": "Как-нибудь 9", "author": "Дж Роллинг 9"},
        {"id": 7, "title": "Как-нибудь 7", "author": "Дж Роллинг 7"},
    ]

    return {
        "recommendations": recs,
        "history": history,
    }
