
class Project:
    def __init__(self,owner,name,lastupdate):
        self.projOwner = owner #string
        self.projName = name #string
        self.lastUpdate = lastupdate #string
        self.userList = ["NoUsers"] #list of dictionaries
        self.houseList = ["NoHouse"] #list

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
     
    ##userList is a list of dictionaries
    def getUserList(self):
        return self.userList 

    def addToUserList(self, user):
        self.userList.append(user)
        return

    ##houseList is a list of dictionaries
    def getHouseList(self):
        return self.houseList 

    def addToHouseList(self, house):
        self.houseList.append(house)
        return
    
