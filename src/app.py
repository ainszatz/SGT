from flask import Flask
from src.routes.book_routes import book_routes
from src.routes.member_routes import member_routes
from src.routes.borrowing_routes import borrowing_routes

app = Flask(__name__)

# Register routes
app.register_blueprint(book_routes)
app.register_blueprint(member_routes)
app.register_blueprint(borrowing_routes)

from src.config.database import init_db  # Import the init_db function

app = Flask(__name__)

# Register routes
app.register_blueprint(book_routes)
app.register_blueprint(member_routes)
app.register_blueprint(borrowing_routes)

# Initialize the database
init_db()  # Call the init_db function to create tables and insert sample data

if __name__ == '__main__':
    app.run(debug=True)
