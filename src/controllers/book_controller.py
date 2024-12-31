from flask import request, jsonify
from src.services.book_service import get_books  # Assuming a service function to fetch books

def get_books_controller():
    title = request.args.get('title', '').lower()
    author = request.args.get('author', '').lower()
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 20))

    books, total = get_books(title, author, page, limit)  # Fetch books from service

    total_pages = (total // limit) + (1 if total % limit > 0 else 0)

    response = {
        "data": books,
        "pagination": {
            "total": total,
            "page": page,
            "limit": limit,
            "totalPages": total_pages
        }
    }
    return jsonify(response)
