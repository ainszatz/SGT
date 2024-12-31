from flask import Blueprint
from src.controllers.book_controller import get_books_controller

book_routes = Blueprint('book_routes', __name__)

# Define the route for getting books
book_routes.route('/api/books', methods=['GET'])(get_books_controller)
