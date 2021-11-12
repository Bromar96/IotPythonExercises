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

    def setLastUpdate(self, last):
        date = last[0:4]+'-'+last[4:6]+'-'+last[6:8]+' '+last[8:10]+':'+last[10:12]
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
            ID= i.getUserID()
            print(f"\t{name} userID: {ID}")
        return 

    def addToUserList(self, user):
        self.userList.append(user)
        return

    def getUserList(self):
        return self.userList

    def readUser(self, f):
        line = f.readline()
        lista=line.split(':')
        name=self.parse(lista[1])   

        line = f.readline()
        lista=line.split(':')
        userID=self.parse(lista[1])

        line = f.readline()
        lista=line.split(':')
        chatID=self.parse(lista[1]) 

        u = self.createUser(name,userID,chatID)
        ##add list of HouseID
        line = f.readline()
        lista=line.split(':')  
        for i in range(len(lista)):
            if "houseID" in lista[i]:
                ID=(lista[i+1][1])
                u.addHouseToUser(ID)       
        return 

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
            print(f"\tUser: {user}")
            u.showHouses()
        return

    def printHousesForUser(self,user):
        for u in self.getUserList(): #self.userList
            if user== int(u.getUserID()):
                u.showHouses()
        return

    def readHouse(self, f):

        userID=""
        houseID=""
        house = 1
        h = self.createHouse(userID,houseID)
        f.readline()
    
        while(house):
            line = f.readline()
            lista = line.split(':')
            if "userID" in lista[0]:
                userID=self.parse(lista[1])
                h.setUserID(userID)
            elif "houseID" in lista[0]:
                houseID=self.parse(lista[1])
                h.setHouseID(houseID)

            elif "devicesList" in lista[0]:
                newDev = h.readDevice(f)
                newID = newDev.getDeviceID()
            elif "}" in lista[0]:
                self.addToHouseList(h)
                house = 0             
        return

    def showDeviceList(self):
        for h in self.houseList:
            ID = h.getHouseID()
            print(f"HouseID: {ID}")
            h.showDevicesInHouse()
        return

    def getHouseByID(self,ID):
        for h in self.houseList:
            hid=h.getHouseID()
            if hid == ID:
                return h
        return ""

    def searchUser(self, userID):
        result = 0
        for u in self.userList:
            uid = int(u.getUserID())
            if uid == userID:
                u.getAllInfo()
                result = 1
        if result == 0:
            print("\t\tERROR: USER NOT FOUND\n")
        return

    def searchDeviceByID(self, devID):
        result = 0
        for h in self.houseList:
            f = h.searchDevice(devID)
            if f == 1:
                result = 1
        if result == 0:
            print("\t\tERROR: DEVICE NOT FOUND\n")

    def searchDeviceByHouseID(self,houseID):
        result = 0
        for h in self.houseList:
            hid= int(h.getHouseID())
            if hid == houseID:
                h.showDevicesInHouse()
                result = 1
        if result == 0:
            print("\t\tERROR: HOUSE NOT FOUND\n")
        return

    def searchDevice(self,typeMT):
        result = 0
        for h in self.houseList:
            f = h.searchTypeInDevice(typeMT)
            if f == 1:
                result = 1
        if result == 0:
            print("\t\tERROR: DEVICE NOT FOUND, probably MEASURE TYPE IS WRONG\n")
        return

    def insertDevice(self,userID,houseID,deviceID):
        #check if the device is already present
        new = 1;
        for d in self.deviceList:
            if d == deviceID:
                new = 0;
        if new == 1:
            ##add house to User
            for u in self.userList:  
                if int(u.getUserID()) == userID:
                    u.pushHouse(houseID)
            ##add Device to House
                
            house = self.getHouseByID(houseID)
            if house == "": ##house doesn't exists
                house = House(userID,houseID)
            house.addDevice(deviceID)
        else:
            house = self.getHouseByID(houseID)
            house.modifyDevice(deviceID)
        return
    
    ##given a string, every character that is not [a-z][A-Z] is deleted
    def parse(self, stringa):
        result=''
        for i in range(len(stringa)):
            if stringa[i].isalnum():
                result = result + stringa[i]
        return result
        
    
