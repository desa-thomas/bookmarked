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
