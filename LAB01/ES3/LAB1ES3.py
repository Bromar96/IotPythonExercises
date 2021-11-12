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


def searchDeviceByID(devID):
    p.searchDeviceByID(devID)
    return

def searchDeviceByHouseID(houseID):
    p.searchDeviceByHouseID(houseID)
    return

def searchUserByUserID(userID):
    p.searchUser(userID)
    return

def searchDevicesByMeasureType(typeMT):
    p.searchDevice(typeMT)
    return

def printAll():
    print("Owner:        ", p.getOwner())
    print("Project name: ", p.getName())
    print("Last update:  ", p.getLastUpdate())
    print("Print users list: ")
    p.printUserList()
    print("Print houses list for each User")
    p.getHouseListOfEachUser()
    print("Print all devices")
    p.showDeviceList()
    return

def closeProgram():
    return

def insertNewDevice():
    user=int(input("Insert the user ID: "))
    house=int(input("Insert the house ID: "))
    device=int(input("Insert the device ID: "))
    p.insertDevice(user,house,device)
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
                    p.readUser(f)
                elif "]," in line:
                    user=0 #user are finished
                    

        elif "houses" in lista[0]:
            house=1
            while(house):
                line=f.readline()
                if '{' in line:
                    p.readHouse(f)
                elif ']' in line:
                    house = 0
                    
            flag = 0        
    f.close()
    print("End of file")

    run = 1
    while run:
        print("\n\nAVAILABLE FEATURES:")
        print("\t1) search device by ID")
        print("\t2) search device by houseID")
        print("\t3) search user by userID")
        print("\t4) search devices by measure type")
        print("\t5) insert new device")
        print("\t6) print the full catalog")
        print("\t7) exit")
        scelta=int(input("Do your choice: "))

        if scelta == 1:
            var1=int(input("Device ID to search: "))
            searchDeviceByID(var1)
        elif scelta == 2:
            var1=int(input("House ID to search: "))
            searchDeviceByHouseID(var1)
        elif scelta == 3:
            var1=int(input("User ID to search: "))
            searchUserByUserID(var1)
        elif scelta == 4:
            measure=input("Measure type to search: ")
            searchDevicesByMeasureType(measure)
        elif scelta == 5:    
            insertNewDevice()
        elif scelta == 6:
            printAll()
        elif scelta == 7:
            closeProgram()
            run = 0
        else:
            print("Choice is not valid!")

    
