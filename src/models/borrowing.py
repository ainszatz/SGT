from sqlalchemy import Column, String, Date, Enum, TIMESTAMP, ForeignKey
import uuid
from src.config.database import Base

class Borrowing(Base):
    __tablename__ = 'borrowings'

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    book_id = Column(String(36), ForeignKey('books.id'), nullable=False)
    member_id = Column(String(36), ForeignKey('members.id'), nullable=False)
    borrow_date = Column(Date, nullable=False)
    return_date = Column(Date)
    status = Column(Enum('BORROWED', 'RETURNED', name='borrowing_status'), default='BORROWED')
    from sqlalchemy import func  # Import func for default timestamp

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
