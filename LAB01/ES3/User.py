##SUBCLASS 1 USER

    
class User:
    def __init__ (self):
        self.userName = ""
        self.userID = ""
        self.chatID = ""
        self.houseList = [] ##The houseID is identified by an integer

    def pushHouse(self, value):
        self.houseList.append(value)
        return
    
    def popHouse(self):
        return self.houseList.pop()

    def popHouseByID(self, index):
        return self.houseList.pop(index)

    def showHouses(self):
        for i in self.houseList:
            print(f"\t\thouseID: {i}")
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

    def addHouseToUser(self,houseID):
        new = int(houseID)
        self.pushHouse(new)
        return
    
    def getAllInfo(self):
        print(f"\tuser name: {self.userName}")
        print(f"\tuserID:    {self.userID}")
        print(f"\tchatID:    {self.chatID}")
        print("\tList of houses ID: ", end='')
        for i in self.houseList:
            print(f"{i} ", end='')
        print('')
        return
    
        
