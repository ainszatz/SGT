from sqlalchemy import create_engine, inspect
from src.config.database import DATABASE_URL

def check_tables():
    engine = create_engine(DATABASE_URL)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)

if __name__ == "__main__":
    check_tables()
