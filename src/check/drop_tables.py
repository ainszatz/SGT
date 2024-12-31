from sqlalchemy import create_engine
from sqlalchemy import create_engine, text
from src.config.database import DATABASE_URL

def drop_tables():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS borrowings CASCADE;"))
        connection.execute(text("DROP TABLE IF EXISTS books CASCADE;"))
        connection.execute(text("DROP TABLE IF EXISTS members CASCADE;"))
        print("Dropped existing tables.")

if __name__ == "__main__":
    drop_tables()
