from House import *
from User import *

class Project:
    def __init__(self,owner,name,lastupdate):
        self.projOwner = owner #string
        self.projName = name #string
        self.lastUpdate = lastupdate #string
        self.userList = [] #list of users
        self.houseList = [] #list of houses 

    ##projOwner is a string
    def getOwner(self):
        return self.projOwner 

    def setOwner(self, owner):
        self.projOwner = owner
        return
    
    ##projName is a string
    def getName(self):
        return self.projName 

    def setName(self, name):
        self.projName = name
        return

    ##lastUpdate is a string
    def getLastUpdate(self):
        return self.lastUpdate 

    def setLastUpdate(self, date):
        self.lastUpdate = date
        return
        
    ##userList is a list of User objects

    def createUser(self, name, userID, chatID):
        u = User()
        u.setName(name)
        u.setUserID(userID)
        u.setChatID(chatID)  
        
        self.addToUserList(u)
        
        return u
    
    def printUserList(self):
        for i in self.userList:
            name = i.getName()
            print(name)
        return 

    def addToUserList(self, user):
        self.userList.append(user)
        return

    def getUserList(self):
        return self.userList

    ##houseList is a list of House objects
    def getHouseList(self):
        return self.houseList

    def addToHouseList(self, house):
        self.houseList.append(house)
        return
    
    def createHouse(self, userID, houseID):
        h = House(userID,houseID) 
        return h

    def getHouseListOfEachUser(self):
        for u in self.getUserList(): #self.userList
            user = u.getName()
            print(f"User: {user}")
            u.showHouses()
        return

    def showDeviceList(self):
        for h in self.houseList:
            ID = h.getHouseID()
            print(f"HouseID: {ID}")
            h.showDevicesInHouse()

        return
        
    
