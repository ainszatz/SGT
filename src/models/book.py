from sqlalchemy import Column, String, Integer, TIMESTAMP, UUID
import uuid
from src.config.database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Change to UUID type
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    published_year = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    from sqlalchemy import func  # Import func for default timestamp

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    isbn = Column(String(13), unique=True, nullable=False)

    def to_dict(self):
        """Convert the Book object to a dictionary."""
        return {
            "id": str(self.id),  # Convert UUID to string
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
            "stock": self.stock,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "isbn": self.isbn,
        }
