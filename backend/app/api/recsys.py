import fastapi
from app.api.models import Recommendation, Book
from app.db import db_manager

recsys = fastapi.APIRouter()


@recsys.get('/recommend/{user_id}', response_model=Recommendation)
async def get_history_and_recs(user_id: int):
    history_records = db_manager.get_user_history(user_id)
    history = []
    recs = []

    if len(history_records) > 0:
        for record in history_records:
            history.append({
                "id": record[0],
                "author": record[1],
                "title": record[2]
            })

        rec_records = db_manager.get_recommendations(user_id)
        for record in rec_records:
            recs.append({
                "id": record[0],
                "author": record[1],
                "title": record[2]
            })

    else:
        popular_records = db_manager.get_popular_books()
        recs = []
        for record in popular_records:
            recs.append({
                "id": record[0],
                "author": record[1],
                "title": record[2]
            })

    return {
        "recommendations": recs,
        "history": history,
    }
