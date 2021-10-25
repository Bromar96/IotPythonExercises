class House:
    def __init__ (self, user, house):
        self.userID = user
        self.houseID = house
        self.deviceList = []

    def getUserID(self):
        return self.userID

    def getHouseID(self):
        return self.houseID

    def getDeviceList(self):
        return self.deviceList
        
