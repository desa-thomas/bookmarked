from datetime import datetime as dt
from controllers.TestController import TestController
#from entities.TestEntity import TestEntity
from entities.Accounts import Account
from entities.Books import Book
from entities.Books import Bookshelf
from entities.Books import ReadingList

tc = TestController()
tc.testFunc()

#te = TestEntity()
#te.testFunc()

ta = Account("User",46327007,"email@email.email","password1234",69,"This is a bio",dt.today().date())
tb = Book("Book",123456789,"John Doe",dt.fromisoformat('1999-06-09').date(),("old","wordy"),"098765-4321",69)
tbs = Bookshelf((tb),46327007,(0),12)
trl = ReadingList("List",101,46327007,(tb),dt.now().time(),True)

showTest = True
if showTest:
    print(ta.getAccountInfo())
    print(tb.getBookDetails())
    print(tbs.getBookshelfDetails())
    print(trl.getListDetails())
