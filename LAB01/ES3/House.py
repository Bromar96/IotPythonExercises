from Device import *

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
        return self.deviceList

    def addDevice(self, device):
        self.deviceList.append(device)
        return

    def popDevice(self):
        return self.deviceList.pop()

    def popDeviceByID(self, ID):
        return self.deviceList.pop(ID)

    def showDevicesInHouse(self):
        for i in self.deviceList:
            i.getAllInfo()

    def parse(self, stringa):
        result=''
        for i in range(len(stringa)):
            if stringa[i].isalnum():
                result = result + stringa[i]
        return result    

    def readDevice(self, f):
        device = 1
        d = Device("","")
        f.readline()
        while(device):
            line=f.readline()
            lista = line.split(':')
            if "deviceID" in line:
                ID = self.parse(lista[1])
                d.setDeviceID(ID)
            elif "deviceName" in line:
                name = self.parse(lista[1])
                d.setDeviceName(name)
            elif "measureType" in line:
                measureList = lista[1].split(',')
                for i in measureList:
                    i = self.parse(i)
                    d.addMeasureType(i)
            elif "availableServices" in line:
                servList = lista[1].split(',')
                for i in servList:
                    i = self.parse(i)
                    d.addService(i)
            elif "servicesDetails" in line:
                d.readServDet(f)
            elif "lastUpdate" in line:
                last=self.parse(lista[1])
                d.setLastUpdate(last)
                device = 0
            
        f.readline() #chiusa graffa
        f.readline() #chiusa quadra
        self.addDevice(d)
        return

    def searchTypeInDevice(self, typeMT):
        for dev in self.deviceList:
            measList=dev.getMeasureTypeList()
            for stringa in measList:

                if typeMT == stringa:
                    dev.getAllInfo()
                    print("\n")
        return

    
        
        
