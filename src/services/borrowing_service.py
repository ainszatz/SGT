from datetime import datetime
import uuid
from src.services.book_service import check_book_stock, update_book_stock
from src.services.member_service import get_member_borrowings_count
from src.models.book import Book  # Import the Book model
from src.models.member import Member  # Import the Member model
from src.models.borrowing import Borrowing  # Import the Borrowing model
from src.config.database import SessionLocal  # Import the database session

def create_borrowing(book_id, member_id):
    with SessionLocal() as db:  # Use the context manager for session management
        # Check if book exists
        book = db.query(Book).filter(Book.id == book_id).first()
        if not book:
            return {"error": "Book not found"}, 404

        # Check if member exists
        member = db.query(Member).filter(Member.id == member_id).first()
        if not member:
            return {"error": "Member not found"}, 404

        # Check book stock
        if book.stock <= 0:
            return {"error": "Book is out of stock"}, 400

        # Check member borrowing limit
        borrow_count = db.query(Borrowing).filter(
            Borrowing.member_id == member_id,
            Borrowing.status == 'BORROWED'
        ).count()
        if borrow_count >= 3:
            return {"error": "Member cannot borrow more than 3 books"}, 400

        # Generate a unique ID
        while True:
            new_id = str(uuid.uuid4())
            existing = db.query(Borrowing).filter(Borrowing.id == new_id).first()
            if not existing:
                break

        # Record the borrowing
        new_borrowing = Borrowing(
            id=new_id,
            book_id=book_id,
            member_id=member_id,
            borrow_date=datetime.now(),
            status='BORROWED'
        )
        db.add(new_borrowing)
        
        # Update book stock
        book.stock -= 1
        
        try:
            db.commit()
            return {"message": f"{member.name} has borrowed {book.title}"}, 201
        except Exception as e:
            db.rollback()
            return {"error": str(e)}, 500

def return_borrowing(borrowing_id):
    with SessionLocal() as db:
        # Get the borrowing record
        borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
        if not borrowing:
            return {"error": "Borrowing not found"}, 404
            
        # Check if already returned
        if borrowing.status == 'RETURNED':
            return {"error": "Book already returned"}, 400
            
        # Update the borrowing record
        borrowing.status = 'RETURNED'
        borrowing.return_date = datetime.now()
        
        # Update book stock
        book = db.query(Book).filter(Book.id == borrowing.book_id).first()
        if book:
            book.stock += 1
            
        try:
            db.commit()
            return {"message": "Book returned successfully"}, 200
        except Exception as e:
            db.rollback()
            return {"error": str(e)}, 500

def get_member_borrowing_history(member_id, status=None, page=1, limit=10):
    with SessionLocal() as db:  # Use the context manager for session management
        query = db.query(Borrowing).filter(Borrowing.member_id == member_id)  # Filter by member ID

        if status:
            query = query.filter(Borrowing.status == status)  # Filter by status if provided

        total = query.count()  # Get the total count of borrowings
        borrowings = query.offset((page - 1) * limit).limit(limit).all()  # Get the paginated borrowings

        # Convert borrowings to a dictionary format, including book details
        borrowings_data = []
        for borrowing in borrowings:
            book = db.query(Book).filter(Book.id == borrowing.book_id).first()  # Get book details
            borrowings_data.append({
                "borrowing_id": borrowing.id,
                "book_id": borrowing.book_id,
                "member_id": borrowing.member_id,
                "borrow_date": borrowing.borrow_date,
                "return_date": borrowing.return_date,
                "status": borrowing.status,
                "book_title": book.title if book else None,  # Include book title
                "book_author": book.author if book else None   # Include book author
            })

        return borrowings_data, total  # Return the borrowings and total count
