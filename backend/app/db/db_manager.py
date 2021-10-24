from app.api.models import MovieIn, MovieOut, MovieUpdate
from app.db.db import conn, history, database


def get_user_history(user_id: int):
    with conn.cursor() as cursor:
        cursor.execute(
            '''
            SELECT h.book_id as id, b.author_fullname as author, b.title_original as title
            FROM history h
                JOIN books b ON h.book_id = b.id
            WHERE user_id = %s
            ORDER BY h.created_on DESC
            ''', (user_id,)
        )
        records = cursor.fetchall()

    return records


def get_popular_books():
    with conn.cursor() as cursor:
        cursor.execute(
            '''
            SELECT rp.book_id as id, b.author_fullname as author, b.title_original as title
            FROM recsys_popular rp
                JOIN books b ON rp.book_id = b.id
            ORDER BY rp.rating ASC
            ''')
        records = cursor.fetchall()

    return records


def get_recommendations(user_id: int):
    with conn.cursor() as cursor:
        cursor.execute(
            '''
            SELECT rpr.book_id as id, b.author_fullname as author, b.title_original as title
            FROM recsys_predictions rpr
                LEFT JOIN history h on h.user_id = rpr.user_id AND rpr.book_id = h.book_id
                JOIN books b ON rpr.book_id = b.id
            WHERE rpr.user_id = %s
            ORDER BY prediction DESC
            LIMIT 5
            ''', (user_id,))

        records = cursor.fetchall()

    return records

# async def get_all_movies():
#     query = movies.select()
#     return await database.fetch_all(query=query)
#
#
# async def get_movie(id):
#     query = movies.select(movies.c.id == id)
#     return await database.fetch_one(query=query)
#
#
# async def delete_movie(id: int):
#     query = movies.delete().where(movies.c.id == id)
#     return await database.execute(query=query)
#
#
# async def update_movie(id: int, payload: MovieIn):
#     query = (
#         movies
#             .update()
#             .where(movies.c.id == id)
#             .values(**payload.dict())
#     )
#     return await database.execute(query=query)
