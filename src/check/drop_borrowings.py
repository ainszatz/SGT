from sqlalchemy import create_engine, text
from src.config.database import DATABASE_URL

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute(text('DROP TABLE IF EXISTS borrowings'))
    print("Borrowings table dropped successfully.")
