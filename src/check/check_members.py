from sqlalchemy import create_engine, text
from src.config.database import DATABASE_URL

engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    result = connection.execute(text('SELECT * FROM members'))
    members = result.fetchall()
    print("Members in the database:")
    for member in members:
        print(member)
