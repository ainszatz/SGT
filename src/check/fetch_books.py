from src.services.book_service import get_books

if __name__ == "__main__":
    books, total = get_books("", "", 1, 10)  # Fetch the first 10 books
    print("Available Books:")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Stock: {book['stock']}")
