##SUBCLASS 1 USER

    
class User:
    def __init__ (self):
        self.userName = ""
        self.userID = ""
        self.chatID = ""
        self.houseList = [] ##The houseID is identified by an integer

    def pushHouse(self, value):
        self.houseList.append(value)
        self.houseList.sort()   
        return
    
    def popHouse(self):
        return self.houseList.pop()

    def popHouseByID(self, index):
        return self.houseList.pop(index)

    def showHouses(self):
        for i in self.houseList:
            print(f"houseID: {i}")
        return

    def getName(self):
        return self.userName

    def setName(self, newName):
        self.userName = newName
        return

    def getUserID(self):
        return self.userID

    def setUserID(self, newUserID):
        self.userID = newUserID
        return

    def getChatID(self):
        return self.chatID

    def setChatID(self, newID):
        self.chatID = newID
        return
    
        
