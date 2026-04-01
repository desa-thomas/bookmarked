from datetime import datetime as dt
from flask import Flask, request, jsonify
from entities.Accounts import Account, ProgressTracker
from entities.Books import Book, Bookshelf, ReadingList
from entities.Social import Forum, Review, FollowingList

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response

#Example data for testing purposes, made one for every entity class. 
#In a real application, this would be replaced with database calls to fetch and store data.
progress = [
    ProgressTracker(
        trackerId=1,
        accountId=1,
        goalId=1,
        currentValue=150,
        targetValue=300,
        lastUpdated=dt.now().date()
    )
]

accounts = [
    Account(
        username="john_doe",
        id=1,
        email="john.doe@example.com",
        passwordHash=hash("password123"),
        profilePicture=b"",
        bio="Just a book lover.",
        creationDate=dt.fromisoformat("2020-01-15").date()
    ),
    Account(
        username="jane_smith",
        id=2,
        email="jane.smith@example.com",
        passwordHash=hash("password456"),
        profilePicture=b"",
        bio="A passionate reader.",
        creationDate=dt.fromisoformat("2020-02-20").date()
    ),
    Account(
        username="alice_jones",
        id=3,
        email="alice.jones@example.com",
        passwordHash=hash("password789"),
        profilePicture=b"",
        bio="Loves mystery novels.",
        creationDate=dt.fromisoformat("2020-03-10").date()
    )

]

books = [
    Book(
        title="Example Book",
        id=1,
        author="Jane Doe",
        publicationDate=dt.fromisoformat("1999-06-09").date(),
        genres=["fiction", "adventure"],
        ISBN="978-0-123456-47-2",
        coverImage=b""
    )
]

shelves = [
    Bookshelf(
        bookmarkedBooks=[books[0]],
        accountId=accounts[0].id,
        readingStatuses=[0,1,2],
        readingGoal=10
    )
]
r_list = [
    ReadingList(
        listName="My Reading List",
        listId=1,
        accountId=accounts[0].id,
        books=[books[0]],
        readingListTimestamp=dt.now().date(),
        listVisibility=True
    )
]

forum = [
    Forum(
        forumId=1,
        forumTitle="General Discussion",
        title="Welcome to the forum!",
        forumTimestamp=dt.now().date()
    )
]

reviews = [
    Review(
        ratingId=1,
        accountId=accounts[0].id,
        ratingAmount=5,
        reviewText="An amazing read! Highly recommended.",
        reviewTimestamp=dt.now().date()
    )
]

f_list = [
    FollowingList(
        followerId=[accounts[0].id],
        followedId=[accounts[1].id],
        dateFollowed=[dt.now().date()]
    )
]

@app.route('/account', methods=['POST'])
def create_account():
    get_data = request.json()
    new_account = Account(
        username=get_data.get('username'),
        id=get_data.get('id'),
        email=get_data.get('email'),
        passwordHash=hash(get_data.get('password')),
        profilePicture=get_data.get('profilePicture'),
        bio=get_data.get('bio'),
        creationDate=dt.now().date()
    )
    accounts.append(new_account)
    return jsonify(new_account.getAccountInfo()),201

@app.route('/book', methods=['POST'])
def create_book():
    get_data = request.json()
    new_book = Book(
        title=get_data.get('title'),
        id=get_data.get('id'),
        author=get_data.get('author'),
        publicationDate=get_data.get('publicationDate'),
        genres=get_data.get('genres'),
        ISBN=get_data.get('ISBN'),
        coverImage=get_data.get('coverImage')
    )
    books.append(new_book)
    return jsonify(new_book.getBookDetails()),201

@app.route('/forum', methods=['POST'])
def create_forum():
    get_data = request.json()
    new_forum = Forum(
        forumId=get_data.get('forumId'),
        forumTitle=get_data.get('forumTitle'),
        title=get_data.get('title'),
        forumTimestamp=dt.now().date()
    )
    forum.append(new_forum)
    return jsonify(new_forum.getForumDetails()),201