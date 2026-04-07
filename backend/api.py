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

progress = [
    ProgressTracker(
        trackerId=1,
        accountId=accounts[0].id,
        goalId=1,
        currentValue=150,
        targetValue=300,
        lastUpdated=dt.now().date()
    )
]

books = [
    Book(
        title="Example Book",
        id=190873,
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
#FOR ACCOUNTS
@app.route('/account', methods=['POST'])
def create_account():
    get_data = request.get_json()
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

@app.route('/accounts', methods=['GET'])
def get_accounts():
    return jsonify([account.getAccountInfo() for account in accounts])

@app.route('/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    account = next((a for a in accounts if a.id == account_id), None)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account.getAccountInfo())

#FOR PROGRESS TRACKER
@app.route('/progress', methods=['POST'])
def create_progress():
    get_data = request.get_json()
    new_progress = ProgressTracker(
        trackerId=get_data.get('trackerId'),
        accountId=get_data.get('accountId'),
        goalId=get_data.get('goalId'),
        currentValue=get_data.get('currentValue'),
        targetValue=get_data.get('targetValue'),
        lastUpdated=dt.now().date()
    )
    progress.append(new_progress)
    return jsonify(new_progress.getProgressDetails()),201

@app.route('/progress', methods=['GET'])
def get_progress():
    return jsonify([p.getProgressDetails() for p in progress])

@app.route('/progress/<int:tracker_id>', methods=['GET'])
def get_progress_tracker(tracker_id):
    tracker = next((p for p in progress if p.trackerId == tracker_id), None)
    if tracker is None:
        return jsonify({"error": "Progress tracker not found"}), 404
    return jsonify(tracker.getProgressDetails())


#FOR BOOKS
@app.route('/book', methods=['POST'])
def create_book():
    get_data = request.get_json()
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

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([book.getBookDetails() for book in books])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b.id == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.getBookDetails())

#FOR BOOKSHELF
@app.route('/bookshelf', methods=['POST'])
def create_bookshelf():
    get_data = request.get_json()
    new_shelf = Bookshelf(
        bookmarkedBooks=get_data.get('bookmarkedBooks'),
        accountId=get_data.get('accountId'),
        readingStatuses=get_data.get('readingStatuses'),
        readingGoal=get_data.get('readingGoal')
    )
    shelves.append(new_shelf)
    return jsonify(new_shelf.getBookshelfDetails()),201

@app.route('/bookshelves', methods=['GET'])
def get_bookshelves():
    return jsonify([shelf.getBookshelfDetails() for shelf in shelves])

@app.route('/bookshelves/<int:account_id>', methods=['GET'])
def get_bookshelf(account_id):
    shelf = next((s for s in shelves if s.accountId == account_id), None)
    if shelf is None:
        return jsonify({"error": "Bookshelf not found"}), 404
    return jsonify(shelf.getBookshelfDetails())

#FOR READING LIST
@app.route('/readinglist', methods=['POST'])
def create_reading_list():
    get_data = request.get_json()
    new_list = ReadingList(
        listName=get_data.get('listName'),
        listId=get_data.get('listId'),
        accountId=get_data.get('accountId'),
        books=get_data.get('books'),
        readingListTimestamp=dt.now().date(),
        listVisibility=get_data.get('listVisibility')
    )
    r_list.append(new_list)
    return jsonify(new_list.getListDetails()),201

@app.route('/readinglists', methods=['GET'])
def get_reading_lists():
    return jsonify([rl.getListDetails() for rl in r_list])

@app.route('/readinglists/<int:list_id>', methods=['GET'])
def get_reading_list(list_id):
    rl = next((r for r in r_list if r.listId == list_id), None)
    if rl is None:
        return jsonify({"error": "Reading list not found"}), 404
    return jsonify(rl.getListDetails())


#FOR FORUM
@app.route('/forum', methods=['POST'])
def create_forum():
    get_data = request.get_json()
    new_forum = Forum(
        forumId=get_data.get('forumId'),
        forumTitle=get_data.get('forumTitle'),
        title=get_data.get('title'),
        forumTimestamp=dt.now().date()
    )
    forum.append(new_forum)
    return jsonify(new_forum.getForumDetails()),201

@app.route('/forums', methods=['GET'])
def get_forums():
    return jsonify([f.getForumDetails() for f in forum])

@app.route('/forums/<int:forum_id>', methods=['GET'])
def get_forum(forum_id):
    f = next((fo for fo in forum if fo.forumId == forum_id), None)
    if f is None:
        return jsonify({"error": "Forum not found"}), 404
    return jsonify(f.getForumDetails())


#FOR REVIEWS
@app.route('/review', methods=['POST'])
def create_review():
    get_data = request.get_json()
    new_review = Review(
        ratingId=get_data.get('ratingId'),
        accountId=get_data.get('accountId'),
        ratingAmount=get_data.get('ratingAmount'),
        reviewText=get_data.get('reviewText'),
        reviewTimestamp=dt.now().date()
    )
    reviews.append(new_review)
    return jsonify(new_review.getReviewDetails()),201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify([r.getReviewDetails() for r in reviews])

@app.route('/reviews/<int:rating_id>', methods=['GET'])
def get_review(rating_id):
    r = next((rev for rev in reviews if rev.ratingId == rating_id), None)
    if r is None:
        return jsonify({"error": "Review not found"}), 404
    return jsonify(r.getReviewDetails())

#FOR FOLLOWING
@app.route('/following', methods=['POST'])
def create_following():
    get_data = request.get_json()
    new_following = FollowingList(
        followerId=get_data.get('followerId'),
        followedId=get_data.get('followedId'),
        dateFollowed=get_data.get('dateFollowed')
    )
    f_list.append(new_following)
    return jsonify({
        "followerId":new_following.getFollowerId(),
        "followedId":new_following.getFollowedId(),
        "dateFollowed":new_following.getDateFollowed()
    }),201

#FOR FOLLOWING LIST
@app.route('/followings', methods=['GET'])
def get_followings():
    return jsonify([{
        "followerId": fl.getFollowerId(),
        "followedId": fl.getFollowedId(),
        "dateFollowed": fl.getDateFollowed()
    } for fl in f_list])

@app.route('/followings/<int:follower_id>', methods=['GET'])
def get_following(follower_id):
    fl = next((f for f in f_list if follower_id in f.getFollowerId()), None)
    if fl is None:
        return jsonify({"error": "Following list not found"}), 404
    return jsonify({
        "followerId": fl.getFollowerId(),
        "followedId": fl.getFollowedId(),
        "dateFollowed": fl.getDateFollowed()
    })
