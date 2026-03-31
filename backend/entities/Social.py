# Coded By: Mateo Adebowale
# Last Edit: 2026/03/30
from datetime import date

class Forum: 
    def __init__(self,forumId:int,forumTitle:str,title:str,forumTimestamp:date) -> None:
        self.forumId = forumId
        self.forumTitle = forumTitle
        self.title = title
        self.forumTimestamp = forumTimestamp 
        return
    def updateForumName(self,newForumTitle:str) -> None:
        self.forumTitle = newForumTitle if newForumTitle else self.forumTitle
        return
    def getForumDetails(self) -> dict:
        return ({
            "forumId":self.forumId,
            "forumTitle":self.forumTitle,
            "title":self.title,
            "forumTimestamp":self.forumTimestamp
        })

class Review: 
    def __init__(self,ratingId:int,accountId:int,ratingAmount:int,reviewText:str,reviewTimestamp:date) -> None:
        self.ratingId = ratingId
        self.accountId = accountId
        self.ratingAmount = ratingAmount
        self.reviewText = reviewText
        self.reviewTimestamp = reviewTimestamp
        return
    def getReviewDetails(self) -> dict:
        return ({
            "ratingId":self.ratingId,
            "accountId":self.accountId,
            "ratingAmount":self.ratingAmount,
            "reviewText":self.reviewText,
            "reviewTimestamp":self.reviewTimestamp
        })

class FollowingList:
    def __init__(self,followerId:list[int],followedId:list[int],dateFollowed:list[date]) -> None:
        self.followerId = followerId
        self.followedId = followedId
        self.dateFollowed = dateFollowed
        return
    def getFollowerId(self) -> list[int]:
        return ({
            "followerID":self.followerId
        })
    def getFollowedId(self) -> list[int]:
        return ({
            "followedID":self.followedId
        })
    def getDateFollowed(self) -> list[date]:
        return ({
            "dateFollowed":self.dateFollowed
        })