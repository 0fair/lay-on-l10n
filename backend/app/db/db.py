import os
import psycopg2

DATABASE_URI = os.getenv('DATABASE_URI')
conn = psycopg2.connect(dbname=os.getenv('POSTGRES_USER'), user=os.getenv('POSTGRES_DB'),
                            password=os.getenv('POSTGRES_PASSWORD'), host='moslib-db')

def disconnect():
    conn.close()
