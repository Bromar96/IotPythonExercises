class House:
    def __init__ (self, user, house):
        self.userID = user
        self.houseID = house
        self.deviceList = []

    def getUserID(self):
        return self.userID

    def setUserID(self, newID):
        self.userID = newID
        return 

    def getHouseID(self):
        return self.houseID

    def setHouseID(self, newID):
        self.houseID = newID
        return 

    def getDeviceList(self):
        return self.deviceList()

    def getPushDevice(self, device):
        self.deviceList.append(device)
        self.deviceList.sort()
        return

    def getPopDevice(self):
        return self.deviceList.pop()

    def getPopDeviceByID(self, ID):
        return self.deviceList.pop(ID)
        
