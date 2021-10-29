## MAIN CLASS
from Project import *
from User import *
from House import *

##given a line of a json file "key": "value", returns only value
def searchStringa(stringa):
    start = 0
    stop = 0
    for i in range(len(stringa)):
        if (stringa[i] == ':') and (start==0) :
            start = i+3
        elif (start != 0) and (stringa[i]=='"') and (stringa[i+1] ==','):
            stop = i
            
    return stringa[start:stop]

##given a string, every character that is not [a-z][A-Z] is deleted
def parse(stringa):
    result=''
    for i in range(len(stringa)):
        if stringa[i].isalnum():
            result = result + stringa[i]
    return result

def readUser(f, p):
    line = f.readline()
    lista=line.split(':')
    name=parse(lista[1])   

    line = f.readline()
    lista=line.split(':')
    userID=parse(lista[1])

    line = f.readline()
    lista=line.split(':')
    chatID=parse(lista[1]) 

    u = p.createUser(name,userID,chatID)
    ##add list of HouseID
    line = f.readline()
    lista=line.split(':')  
    for i in range(len(lista)):
        if "houseID" in lista[i]:
            ID=(lista[i+1][1])
            u.addHouseToUser(ID)       
    return 

def readHouse(f, p):

    userID=""
    houseID=""
    house = 1
    h = p.createHouse(userID,houseID)
    f.readline()
    
    while(house):
        line = f.readline()
        lista = line.split(':')
        if "userID" in lista[0]:
            userID=parse(lista[1])
            h.setUserID(userID)
        elif "houseID" in lista[0]:
            houseID=parse(lista[1])
            h.setHouseID(houseID)

        elif "devicesList" in lista[0]:
            h.readDevice(f)
##        elif "lastUpdate" in lista[0]:
##            last = parse(lista[1])
##            h.setLastUpdate(last)
        elif "}" in lista[0]:
            p.addToHouseList(h)
            house = 0             
    return

def searchDeviceByID(devID):
    hList=p.getHouseList()
    for h in hList:
        devList = h.getDeviceList()
        for d in devList:
            ID = int(d.getDeviceID())
            if ID == devID:
                d.getAllInfo()
    
    return

def searchDeviceByHouseID(houseID):
    return

def searchUserByUserID(userID):
    return
def searchDevicesByMeasureType(typeMT):
    return

def insertDevice():
    return

def printAll():
    return
def exit():
    return




if __name__=="__main__":
    f=open("catalog.json")
    f.readline() ##first line is useless
    flag = 1
    p = Project("","","")
     
    while(flag):
        line=f.readline()
        lista=line.split(':')
        
        if "projectOwner" in lista[0]:  
            owner=parse(lista[1])
            p.setOwner(owner)

        elif "projectName" in lista[0]:
            name=parse(lista[1])
            p.setName(name)

        elif "lastUpdate" in lista[0]:
            update=parse(lista[1]+lista[2])
            p.setLastUpdate(update)
    
        elif "usersList" in lista[0]:
            user=1
            while(user):
                line=f.readline()
                if '{' in line:
                    readUser(f, p)
                elif "]," in line:
                    user=0 #user are finished
                    

        elif "houses" in lista[0]:
            house=1
            while(house):
                line=f.readline()
                if '{' in line:
                    readHouse(f,p)
                elif ']' in line:
                    house = 0
                    
            flag = 0        
    
    print("Owner: ", p.getOwner())
    print("Project name: ", p.getName())
    print("Last update: ", p.getLastUpdate())
    
    print("Print users list")
    p.printUserList()
    print("Print houses list for each User")
    p.getHouseListOfEachUser()
    print("print all devices")
    p.showDeviceList()

    searchDeviceByID(2)
##    print(p.getUserList())
##    print(p.getHouseList())
##    h = House(24,1)
##
##    p.addToHouseList(h)
##    
##    newHouse = p.getHouseList().pop()
##
##    print(newHouse.getUserID())


    
    ##if(line= "}"):
    f.close()
    print("End of file")
