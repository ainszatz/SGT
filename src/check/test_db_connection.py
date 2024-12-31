from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from src.config.database import DATABASE_URL

def test_db_connection():
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        print("Database connection successful!")
        connection.close()
    except SQLAlchemyError as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    test_db_connection()
