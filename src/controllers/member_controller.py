from flask import request, jsonify
from src.services.borrowing_service import get_member_borrowing_history
from src.services.member_service import register_member
from src.models.member import Member

def register_member_controller():
    data = request.get_json()
    response = register_member(data)  # Call the service to register the member
    
    # Check if the response contains the 'member' key
    if "member" in response:
        member_id = response["member"]["id"]  # Access the member ID from the dictionary
        member_name = response["member"]["name"]  # Access the member name from the dictionary
        member_email = response["member"]["email"]  # Access the member email from the dictionary
        return jsonify({
            "message": "New member created.",
            "member_id": member_id,
            "name": member_name,
            "email": member_email
        }), 201
    else:
        # Return the error message if 'member' key is not present
        return jsonify({
            "message": response.get("message", "Failed to create member."),
            "error": response.get("error", "Unknown error occurred.")
        }), 400

def get_member_borrowings_controller(member_id):
    status = request.args.get('status')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    # Get member details
    from src.config.database import SessionLocal
    with SessionLocal() as db:
        member = db.query(Member).filter(Member.id == member_id).first()
        if not member:
            return jsonify({"error": "Member not found"}), 404

    borrowings, total = get_member_borrowing_history(member_id, status, page, limit)
    total_pages = (total + limit - 1) // limit
    
    return jsonify({
        "memberId": member_id,
        "memberName": member.name,
        "status": status,
        "page": page,
        "limit": limit,
        "totalRecords": total,
        "totalPages": total_pages,
        "borrowings": borrowings
    }), 200
