##subclass 3 Device 

class Device:
    def __init__(self, ID, name):
        self.deviceID = ID
        self.deviceName = name
        self.measureType = []
        self.availableServices = []
        self.lastUpdate = ""

    def addService(self, service):
        self.availableServices.append(service)
        return

    def showServices(self):
        for i in self.availableServices:
            print(i)
        return

    def popService(self):
        return self.availableServices.pop()

    def getServices(self):
        return self.availableServices
    
    def getDeviceID(self):
        return self.deviceID

    def setDeviceID(self, ID):
        self.deviceID = ID
        return

    def getDeviceName(self):
        return self.deviceName

    def setDeviceName(self, name):
        self.deviceName = name
        return

    def getLastUpdate(self):
        return self.lastUpdate

    def setLastUpdate(self, last):
        self.lastUpdate = last
        return
    
    def addMeasureType(self, measure):
        self.measureType.append(measure)
        return
    def showMeasureType(self):
        for i in self.measureType:
            print(i)
        return

    def getMeasureTypeList(self):
        return self.measureType

    def getAllInfo(self):
        ID = self.deviceID
        name = self.deviceName
        print(f"DeviceID: {ID}")
        print(f"Device name: {name}")
        print("Measure types:")
        for m in self.measureType:
            print(m)
        print("Available Services:")
        for s in self.availableServices:
            print(s)
        last = self.lastUpdate
        print(f"last update: {last}")
        return

        
