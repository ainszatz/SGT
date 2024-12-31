from sqlalchemy import create_engine
from src.config.database import DATABASE_URL

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute('TRUNCATE TABLE borrowings, books RESTART IDENTITY CASCADE;')
