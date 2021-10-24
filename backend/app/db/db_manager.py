from app.db.db import conn


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
            WHERE rpr.user_id = %s AND h.book_id IS NULL
            ORDER BY prediction DESC
            LIMIT 5
            ''', (user_id,))

        records = cursor.fetchall()

    return records