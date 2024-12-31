from sqlalchemy.orm import Session
from src.config.database import SessionLocal
from src.services.book_service import get_books
from src.services.borrowing_service import borrow_book, return_book
from src.models.book import Book
from src.models.borrowing import Borrowing
from datetime import date
import random  # Importing random to generate valid ISBNs

def generate_isbn():
    return ''.join([str(random.randint(0, 9)) for _ in range(13)])  # Generate a 13-digit ISBN

def test_get_books():
    db: Session = SessionLocal()
    try:
        books, total = get_books("", "", 1, 10)  # Fetch all books
        print(f"Total books retrieved: {total}")
        print("Books:", books)
    finally:
        db.close()

def test_borrow_book():
    db: Session = SessionLocal()
    try:
        # Setup: Create a book and a member for testing
        unique_isbn = generate_isbn()  # Generate a valid 13-digit ISBN
        book = Book(title="Test Book", author="Author", published_year=2021, stock=5, isbn=unique_isbn)
        db.add(book)
        db.commit()
        db.refresh(book)

        # Test borrowing the book
        result = borrow_book(member_id="test_member_id", book_id=book.id)
        assert "id" in result  # Check if borrowing was successful

        # Test borrowing when stock is 0
        book.stock = 0
        db.commit()
        result = borrow_book(member_id="test_member_id", book_id=book.id)
        assert "error" in result  # Check for error when book is not available

        # Test borrowing when member has reached limit (mocking member's borrowing count)
        # This part will depend on how the member's borrowing count is managed

    finally:
        db.close()

def test_return_book():
    db: Session = SessionLocal()
    try:
        # Setup: Create a book and a borrowing record for testing
        unique_isbn = generate_isbn()  # Generate a valid 13-digit ISBN
        book = Book(title="Test Book", author="Author", published_year=2021, stock=5, isbn=unique_isbn)
        db.add(book)
        db.commit()
        db.refresh(book)

        borrowing_record = Borrowing(book_id=book.id, member_id="test_member_id", borrow_date=date.today())
        db.add(borrowing_record)
        db.commit()
        db.refresh(borrowing_record)

        # Test returning the book
        result = return_book(borrowing_id=borrowing_record.id)
        assert result["status"] == "RETURNED"  # Check if return was successful

        # Test returning a non-existent borrowing record
        result = return_book(borrowing_id="non_existent_id")
        assert "error" in result  # Check for error when borrowing record does not exist

    finally:
        db.close()

if __name__ == "__main__":
    test_get_books()
    test_borrow_book()
    test_return_book()
