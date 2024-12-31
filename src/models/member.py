from sqlalchemy import Column, String, TEXT, TIMESTAMP
import uuid
from src.config.database import Base

class Member(Base):
    __tablename__ = 'members'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))  # Use a callable to generate a new UUID
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)
    address = Column(TEXT, nullable=False)
    from sqlalchemy import func  # Import func for default timestamp

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
