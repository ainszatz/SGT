# Library Management System

## Project Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python src/init_db.py
   ```

4. Run the application:
   ```bash
   python src/app.py
   ```

## API Documentation

### 1. GET /api/books
List all books with their current stock

**Response Format:**
```json
{
  "data": [{
    "author": "J.R.R. Tolkien",
    "created_at": "Tue, 31 Dec 2024 02:25:35 GMT",
    "id": "045c4949-1880-4560-a717-362bb5986597",
    "isbn": "9780618640157",
    "published_year": 1954,
    "stock": 3,
    "title": "The Lord of the Rings",
    "updated_at": "Tue, 31 Dec 2024 11:47:00 GMT"
  }],
  "pagination": {
    "limit": 20,
    "page": 1,
    "total": 20,
    "totalPages": 1
  }
}
```

### 2. POST /api/members
Register new member

**Request Body:**
```json
{
  "email": "karina@example.com",
  "member_id": "6277f0ee-5c32-4265-bf4f-c2e16ee9b460",
  "message": "New member created.",
  "name": "Karina"
}
```

**Validations:**
- Email must be unique and valid format
- Phone must be valid format
- All fields are required

### 3. POST /api/borrowings
Create new book borrowing

**Request Body:**
```json
{
  "message": "{member_name} has borrowed {book_name}"
}
```

**Business Rules:**
- Check book stock (must be > 0)
- Update book stock (-1)
- Member cannot borrow more than 3 books
- Record borrowing date as current date

### 4. PUT /api/borrowings/:id/return
Process book return

**Path Parameters:**
- `id`: Borrowing ID

**Response Format:**
```json
{
  "message": "Book returned successfully"
}
```

**Updates:**
- Change status to 'RETURNED'
- Update book stock (+1)
- Set return_date to current date

### 5. GET /api/members/:id/borrowings
Get member's borrowing history

**Path Parameters:**
- `id`: Member ID

**Query Parameters:**
- `status`: Filter by status (BORROWED/RETURNED)
- `page` (integer, default: 1)
- `limit` (integer, default: 10)

**Response includes book details**
