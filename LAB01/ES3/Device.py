##subclass 3 Device 

class Device:
    def __init__(self, ID, name):
        self.deviceID = ID
        self.deviceName = name
        self.measureType = []
        self.availableServices = []
        self.servicesDetails=[] #list of dictionaries
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
        date = last[0:4]+'-'+last[4:6]+'-'+last[6:8]
        self.lastUpdate = date
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
        print(f"\tDeviceID: {ID}")
        print(f"\tDevice name: {name}")
        print(f"\tMeasure types: ", end='')
        for m in self.measureType:
            print(f"{m} ", end='')
        print("")
        print("\tAvailable Services: ", end='')
        for s in self.availableServices:
            print(f"{s} ", end='')
        print('')
        print("\tServices details: ")
        for s in self.servicesDetails:
            diz=s.items()
            for d in diz:
                print(f"\t\t{d}")
        last = self.lastUpdate
        print(f"\tlast update: {last}")
        return

    def readServDet(self,f):
        f.readline()
        det=1
        st=0
        si=0
        t=0
        diz={}
        while(det):
            line=f.readline()
            lista = line.split(':')
            if "serviceType" in line:
                serTypeVal=self.parse(lista[1])
                serTypeKey="serviceType"
                serviceType = {serTypeKey:serTypeVal}
                st=1
            elif "serviceIP" in line:
                serIPKey="serviceIP"    
                if len(lista) > 2:
                    ##is an IP address
                    lista[1]+=" "
                    IP = lista[1][2:-1]
                    for i in range(len(lista[2])):
                        if lista[2][i] == '"':
                            stop = i
                    port= lista[2][0:stop]
                    add = IP+":"+port
                    serIPVal=add
                else:
                    ##is an URL
                    serIPVal=self.parseURL(lista[1])
                serviceIP = {serIPKey:serIPVal}
                si=1
            elif "topic" in line:
                topicList=lista[1].split(',')
                topVal =[]
                for h in topicList:
                    topVal.append(self.parseURL(h))
                    topKey="topic"
                    topic ={topKey:topVal}
                t=1
            elif "}" in line:
                if(st==1):
                    diz.update(serviceType)
                if(si==1):
                    diz.update(serviceIP)
                if(t==1):
                    diz.update(topic)
                self.servicesDetails.append(diz)
                line=f.readline()
                if "]," in line:
                    det = 0
        return

    def parse(self, stringa):
        result=''
        for i in range(len(stringa)):
            if stringa[i].isalnum():
                result = result + stringa[i]
        return result  
    

    def parseURL(self,stringa):
        start = 0
        stop = 0
        for i in range(len(stringa)):
            if (stringa[i] == '"'):
                if start==0:
                    start = i+1
                else:
                    stop = i
        return stringa[start:stop]
    
