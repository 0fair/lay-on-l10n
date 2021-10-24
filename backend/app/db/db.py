import os

from sqlalchemy import MetaData, create_engine, ARRAY, BigInteger, Boolean, Column, Date, Enum, Float, Index, Integer, String, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base
from databases import Database
import psycopg2

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()
Base = declarative_base()

conn = psycopg2.connect(dbname=os.getenv('POSTGRES_USER'), user=os.getenv('POSTGRES_DB'),
                        password=os.getenv('POSTGRES_PASSWORD'), host='moslib-db')



class Book(Base):
    __tablename__ = 'books'

    id = Column(BigInteger, primary_key=True)
    author_fullname = Column(Text)
    title_original = Column(Text)
    collapse_parent_id = Column(BigInteger)
    is_collection = Column(Boolean)
    collapse_id = Column(BigInteger)
    parent_id = Column(BigInteger)
    publication_type = Column(Text)
    norm_part = Column(Integer)


history = Table(
    'history', metadata,
    Column('user_id', BigInteger, nullable=False),
    Column('book_id', BigInteger, nullable=False),
    Column('event', Enum('add', 'create_order', 'issue', name='event_enum'), nullable=False),
    Column('created_on', Date),
    Index('history_index', 'user_id', 'book_id')
)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, server_default=text("nextval('movies_id_seq'::regclass)"))
    name = Column(String(50))
    plot = Column(String(250))
    genres = Column(ARRAY(String()))
    casts_id = Column(ARRAY(Integer()))


class RecsysPopular(Base):
    __tablename__ = 'recsys_popular'

    book_id = Column(BigInteger)
    rating = Column(BigInteger, primary_key=True)


t_recsys_predictions = Table(
    'recsys_predictions', metadata,
    Column('user_id', BigInteger),
    Column('book_id', BigInteger),
    Column('prediction', Float)
)

database = Database(DATABASE_URI)
