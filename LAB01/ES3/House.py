from Device import *
from datetime import datetime

class House:
    def __init__ (self, user, house):
        self.userID = user
        self.houseID = house
        self.deviceList = []  ##list of Devices

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
        self.deviceList.append(d)
        return d

    def searchDevice(self,deviceID):
        f = 0
        for d in self.deviceList:
            if d.getDeviceID() == deviceID:
                d.getAllInfo()
                f = 1
        return f  

    def searchTypeInDevice(self, typeMT):
        res = 0
        for dev in self.deviceList:
            measList=dev.getMeasureTypeList()
            for stringa in measList:
                if typeMT == stringa:
                    dev.getAllInfo()
                    print("\n")
                    res=1
        return res

    
    def modifyDevice(self,devID):
        for d in self.deviceList:
            if d.getDeviceID() == devID:
                d.getAllInfo()
                print("PRINT ALL PARAMETERS of Device")
                d.printParameters()
                param = input("What parameter to modify?")

                d.modifyParam(param)
                
                today = str(datetime.today())
                new.update(today[0:10])
        return

    def addDevice(self,devID):
        new = Device(devID,"")
        name=input("\tInsert name of your device: ")
        new.setDeviceName(name)
        flag = 1
        print("\tInsert list of measure type, -1 to finish")
        while(flag):
            mt = input("\t")
            if mt == "-1":
                flag = 0
            else:
                new.addMeasureType(mt)
        flag = 1
        print("\tInsert list of available services, -1 to finish")
        while(flag):
            mt = input("\t")
            if mt == "-1":
                flag = 0
            else:
                new.addService(mt)

        new.addServicesDetails()
        
        today = str(datetime.today())
        print(today[0:10])
        new.update(today[0:10])
        self.deviceList.append(new)
        return 
        
