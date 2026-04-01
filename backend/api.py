from datetime import datetime as dt
from flask import Flask, request, jsonify

from entities.Accounts import Account
from entities.Books import Book
from entities.Books import Bookshelf
from entities.Books import ReadingList

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response

# In-memory sample data for initial testing
books = [
    Book(
        title="Example Book",
        id=1,
        author="Jane Doe",
        publicationDate=dt.fromisoformat("1999-06-09").date(),
        genres=["fiction", "adventure"],
        ISBN="978-0-123456-47-2",
        coverImage=b""
    ),
    Book(
        title="Another Book",
        id=2,
        author="John Smith",
        publicationDate=dt.fromisoformat("2005-09-15").date(),
        genres=["non-fiction", "history"],
        ISBN="978-0-987654-32-1",
        coverImage=b""
    )
]

bookshelves = [
    Bookshelf(
        bookmarkedBooks=[books[0]],
        accountId=1,
        readingStatuses=[0],
        readingGoal=10
    )
]

readingList = [
    ReadingList(
        listName="My Reading List",
        listId=1,
        accountId=1,
        books=[books[0]],
        readingListTimestamp=dt.today().date(),
        listVisibility=True
    )
]

accounts = [
    Account(
        username="testuser",
        id=1,
        email="test@example.com",
        passwordHash="password1234",
        profilePicture=b"",
        bio="This is a bio",
        creationDate=dt.today().date()
    )
]


def serialize_book(book: Book) -> dict:
    return {
        "title": book.title,
        "id": book.id,
        "author": book.author,
        "publicationDate": str(book.publicationDate),
        "genres": book.genres,
        "ISBN": book.ISBN,
    }


def serialize_account(account: Account) -> dict:
    return {
        "username": account.username,
        "accountId": account.id,
        "email": account.email,
        "bio": account.bio,
        "creationDate": str(account.creationDate),
    }


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify([serialize_book(book) for book in books])


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(serialize_book(book))


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json() or {}
    publication_date = None
    if data.get("publicationDate"):
        publication_date = dt.fromisoformat(data["publicationDate"])

    book.updateBookInfo(
        newTitle=data.get("title"),
        newAuthor=data.get("author"),
        newPublicationDate=publication_date,
        newGenres=data.get("genres"),
        ISBN=data.get("ISBN")
    )
    return jsonify(serialize_book(book))


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    index = next((i for i, b in enumerate(books) if b.id == book_id), None)
    if index is None:
        return jsonify({"error": "Book not found"}), 404
    books.pop(index)
    return jsonify({"message": "Book deleted"}), 200


@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json() or {}
    new_id = max((book.id for book in books), default=0) + 1
    book = Book(
        title=data.get("title", "Untitled"),
        id=new_id,
        author=data.get("author", "Unknown"),
        publicationDate=dt.today().date(),
        genres=data.get("genres", []),
        ISBN=data.get("ISBN", ""),
        coverImage=b""
    )
    books.append(book)
    return jsonify(serialize_book(book)), 201


@app.route("/accounts", methods=["GET"])
def get_accounts():
    return jsonify([serialize_account(account) for account in accounts])


@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    account = next((a for a in accounts if a.id == account_id), None)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(serialize_account(account))


@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    account = next((a for a in accounts if a.id == account_id), None)
    if account is None:
        return jsonify({"error": "Account not found"}), 404

    data = request.get_json() or {}
    account.updateAccount(
        newUsername=data.get("username"),
        newEmail=data.get("email"),
        newProfilePicture=None,
        newbio=data.get("bio")
    )
    if data.get("password"):
        account.changePassword(data["password"])

    return jsonify(serialize_account(account))


@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    index = next((i for i, a in enumerate(accounts) if a.id == account_id), None)
    if index is None:
        return jsonify({"error": "Account not found"}), 404
    accounts.pop(index)
    return jsonify({"message": "Account deleted"}), 200


@app.route("/accounts", methods=["POST"])
def create_account():
    data = request.get_json() or {}
    new_id = max((account.id for account in accounts), default=0) + 1
    account = Account(
        username=data.get("username", "guest"),
        id=new_id,
        email=data.get("email", "guest@example.com"),
        passwordHash=data.get("password", ""),
        profilePicture=b"",
        bio=data.get("bio", ""),
        creationDate=dt.today().date(),
    )
    accounts.append(account)
    return jsonify(serialize_account(account)), 201


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

