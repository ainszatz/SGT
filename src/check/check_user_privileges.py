from sqlalchemy import create_engine
from src.config.database import DATABASE_URL

def check_user_privileges():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute("SELECT current_user;")
        user = result.fetchone()[0]
        print(f"Current user: {user}")

if __name__ == "__main__":
    check_user_privileges()
