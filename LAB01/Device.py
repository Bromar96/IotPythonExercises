##subclass 3 Device 

class Device:
    def __init__(self, ID, name,lastUpdate):
        self.deviceID = ID
        self.deviceName = name
        self.measureType = []
        self.availableServices = []
        self.lastUpdate = lastUpdate

    def pushService(self, service):
        self.availableServices.append(service)
        return

    def popService(self):
        return self.availableServices.pop()

    def getServices(self):
        return self.availableServices

    def getMeasureTypeList(self):
        return self.measureType
    
    def getDeviceID(self):
        return self.deviceID

    def getDeviceName(self):
        return self.deviceName

    def getLastUpdate(self):
        return self.lastUpdate


        
