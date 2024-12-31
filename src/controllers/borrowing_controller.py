from flask import request, jsonify
from src.services.borrowing_service import create_borrowing, get_member_borrowing_history, return_borrowing  # Import the necessary functions

import uuid

def create_borrowing_controller():
    data = request.get_json()
    
    # Validate request data
    if not data or 'member_id' not in data or 'book_id' not in data:
        return jsonify({"error": "Missing required fields: member_id and book_id"}), 400
        
    try:
        # Validate UUID format
        member_id = str(uuid.UUID(data['member_id']))
        book_id = str(uuid.UUID(data['book_id']))
    except ValueError:
        return jsonify({"error": "Invalid UUID format for member_id or book_id"}), 400
    
    result, status_code = create_borrowing(book_id, member_id)  # Call the service to borrow the book
    if status_code != 201:
        return jsonify(result), status_code  # Return error response if borrowing fails

    return jsonify(result), status_code

def return_borrowing_controller(borrowing_id):
    # Process the return of a book
    result, status_code = return_borrowing(borrowing_id)
    return jsonify(result), status_code

def get_member_borrowing_history_controller(member_id):
    status = request.args.get('status')  # Get the status from query parameters
    page = request.args.get('page', default=1, type=int)  # Get the page number, default to 1
    limit = request.args.get('limit', default=10, type=int)  # Get the limit, default to 10

    borrowings, total = get_member_borrowing_history(member_id, status, page, limit)  # Call the service to get borrowings
    return jsonify({"borrowings": borrowings, "total": total}), 200
