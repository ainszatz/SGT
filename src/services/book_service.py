def get_books(title, author, page, limit):
    from src.config.database import SessionLocal  # Import the database session
    from src.models.book import Book  # Import the Book model

    db = SessionLocal()  # Create a new database session
    query = db.query(Book)  # Start a query on the Book model

    # Apply filters based on title and author if provided
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))

    # Pagination
    total = query.count()  # Get the total count of books
    books = query.offset((page - 1) * limit).limit(limit).all()  # Get the paginated books

    books = [book.to_dict() for book in books]  # Convert each book to a dictionary
    db.close()  # Close the database session
    return books, total

def check_book_stock(book_id):
    from src.config.database import SessionLocal  # Import the database session
    from src.models.book import Book  # Import the Book model

    with SessionLocal() as db:  # Use the context manager for session management
        book = db.query(Book).filter(Book.id == book_id).first()  # Get the book by ID
        if book and book.stock > 0:  # Check if the book exists and has stock
            return True
    return False  # Return False if the book was not found or has no stock

def update_book_stock(book_id, amount):
    from src.models.book import Book  # Import the Book model
    from src.config.database import session_scope  # Import the session_scope

    with session_scope() as db:  # Use the context manager for session management
        book = db.query(Book).filter(Book.id == book_id).first()  # Get the book by ID
        if book:
            book.stock += amount  # Update the stock
            db.commit()  # Commit the transaction
            return True
        return False  # Return False if the book was not found
