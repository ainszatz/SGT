from contextlib import contextmanager
from src.config.database import SessionLocal  # Import the database session
from src.models.member import Member  # Import the Member model
from src.models.borrowing import Borrowing  # Import the Borrowing model

@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session for use
    finally:
        db.close()  # Close the database session

def register_member(data):
    """Register a new member."""
    with session_scope() as db:
        new_member = Member(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            address=data.get("address")
        )
        db.add(new_member)  # Add the new member to the session
        db.commit()  # Commit the session to save the member
        return {"member": {"id": str(new_member.id), "name": new_member.name, "email": new_member.email}}  # Return the created member details

def get_members():
    with session_scope() as db:  # Use the context manager for session management
        members = db.query(Member).all()  # Get all members
        return [{"id": str(member.id), "name": member.name} for member in members]  # Return a list of members

def get_member_borrowings_count(member_id):
    with session_scope() as db:  # Use the context manager for session management
        count = db.query(Borrowing).filter(Borrowing.member_id == member_id).count()  # Get the count of borrowings for the member
    return count  # Return the count
