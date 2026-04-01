# Coded By: Mateo Adebowale
# Last Edit: 2026/03/30
from datetime import datetime as dt
from controllers.TestController import TestController
from entities.Accounts import Account
from entities.Accounts import ProgressTracker
from entities.Books import Book
from entities.Books import Bookshelf
from entities.Books import ReadingList
from entities.Social import Forum
from entities.Social import Review
from entities.Social import FollowingList


# Controllers
tc = TestController()
tc.testFunc()

# Entities
showTest = True

if showTest:
    acc = 46327007

    ta = Account("User",acc,"email@email.email","password1234",69,"This is a bio",dt.today().date())
    tb = Book("Book",123456789,"John Doe",dt.fromisoformat('1999-06-09').date(),("old","wordy"),"098765-4321",69)
    tbs = Bookshelf((tb,tb),acc,(0,0),12)
    tf = Forum(710034,"Forum","Book",dt.today().date())
    trl = ReadingList("List",101,acc,(tb,tb),dt.now().time(),True)
    tr = Review(16289714,acc,4,"Good Book",dt.now().time())
    tfl = FollowingList((54305,17710),(54305,15751),(dt.today().date(),dt.fromisoformat('2024-03-16').date()))
    tpt = ProgressTracker(13579,acc,420,5,12,dt.now())

    print(ta.getAccountInfo())
    print(tb.getBookDetails())
    print(tbs.getBookshelfDetails())
    print(tf.getForumDetails())
    print(trl.getListDetails())
    print(tr.getReviewDetails())
    print(tfl.getFollowedId(),tfl.getFollowerId(),tfl.getDateFollowed())
    print(tpt.getProgressDetails())