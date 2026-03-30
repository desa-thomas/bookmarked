from datetime import date

class Book: 
    def __init__(self,title:str,id:int,author:str,publicationDate:int,genres:list[str],ISBN:str,coverImage:bytes) -> None:
        self.title = title
        self.id = id
        self.author = author
        self.publicationDate = publicationDate
        self.genres = genres
        self.ISBN = ISBN
        self.coverImage = coverImage 
        return
    def updateBookInfo(self,newTitle:str,newAuthor:str,newPublicationDate:date,newGenres:list[str],ISBN:str) -> None:
        self.title = newTitle if newTitle else self.title
        self.author = newAuthor if newAuthor else self.author
        self.publicationDate = newPublicationDate if newPublicationDate else self.publicationDate
        self.genres = newGenres if newGenres else self.genres
        self.ISBN = ISBN if ISBN else self.ISBN
        return
    def getBookDetails(self) -> dict:
        return ({
            "title":self.title,
            "id":self.id,
            "author":self.author,
            "publicaitonDate":self.publicationDate,
            "genres":self.genres,
            "ISBN":self.ISBN
        })

class Bookshelf: 
    def __init__(self,bookmarkedBooks:list[Book],accountId:int,readingStatuses:list[int],readingGoal:int) -> None:
        self.bookmarkedBooks = bookmarkedBooks
        self.accountId = accountId
        self.readingStatuses = readingStatuses
        self.readingGoal = readingGoal 
        return
    def getBookshelfDetails(self) -> dict:
        return ({
            "bookmarkedBooks":self.bookmarkedBooks,
            "accountId":self.accountId,
            "readingStatuses":self.readingStatuses,
            "readingGoal":self.readingGoal
        })

class ReadingList: 
    def __init__(self,listName:str,listId:int,accountId:int,books:list[Book],readingListTimestamp:date,listVisibility:bool) -> None:
        self.listName = listName
        self.listId = listId
        self.accountId = accountId
        self.books = books
        self.readingListTimestamp = readingListTimestamp
        self.listVisibility = listVisibility
        return
    def getBookCount(self) -> int:
        return len(self.books)
    def getList(self) -> list[Book]:
        return self.books
    def getListDetails(self) -> dict:
        return ({
            "listName":self.listName,
            "listId":self.listId,
            "accountId":self.accountId,
            "books":self.books,
            "readingListTimestamp":self.readingListTimestamp,
            "listVisibility":self.listVisibility,
            "bookCount":len(self.books) if not isinstance(self.books,Book) else 1 
        })