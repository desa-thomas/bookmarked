# Coded By: Mateo Adebowale
# Last Edit: 2026/03/30
from datetime import date

class Account: 
    def __init__(self,username:str,id:int,email:str,passwordHash:str,profilePicture:bytes,bio:str,creationDate:date) -> None:
        self.username = username
        self.id = id
        self.email = email
        self.passwordHash = passwordHash
        self.profilePicture = profilePicture
        self.bio = bio
        self.creationDate = creationDate
        return
    def updateAccount(self,newUsername:str,newEmail:str,newProfilePicture:bytes,newbio:str) -> None:
        self.username = newUsername if newUsername else self.username
        self.email = newEmail if newEmail else self.email
        self.profilePicture = newProfilePicture if newProfilePicture else self.profilePicture
        self.bio = newbio if newbio else self.bio
        return
    def changePassword(self,newPassword:str) -> None:
        self.passwordHash = hash(newPassword)
        return
    def getAccountInfo(self) -> dict:
        return ({
            "username":self.username,
            "accountId":self.id,
            "email":self.email,
            "profilePicture":self.profilePicture,
            "bio":self.bio,
            "creationDate":self.creationDate
        })

class ProgressTracker:
    def __init__(self,trackerId:int,accountId:int,goalId:int,currentValue:int,targetValue:int,lastUpdated:date) -> None:
        self.trackerId = trackerId
        self.accountId = accountId
        self.goalId = goalId
        self.currentValue = currentValue
        self.targetValue = targetValue
        self.lastUpdated = lastUpdated
        return
    def updateProgress(self,newValue:int) -> None:
        self.currentValue = newValue if newValue else self.currentValue
        return
    def calculateProgressPercentage(self) -> float:
        return 0 if self.targetValue == 0 else round((self.currentValue/self.targetValue)*100,2)
    def isGoalCompleted(self) -> bool:
        return True if self.currentValue >= self.targetValue else False
    def getProgressDetails(self) -> dict:
        return ({
            "trackerId":self.trackerId,
            "userId":self.accountId,
            "goalId":self.goalId,
            "currentValue":self.currentValue,
            "targetValue":self.targetValue,
            "progress":self.calculateProgressPercentage(),
            "completed":self.isGoalCompleted(),
            "lastUpdated":self.lastUpdated
        })