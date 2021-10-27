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
    
    for i in range(2):
        line = f.readline()
        lista = line.split(':')
        if "userID" in lista[0]:
            userID=parse(lista[1])
        elif "houseID" in lista[0]:
            houseID=parse(lista[1])

    h = p.createHouse(userID,houseID)
    line = f.readline()
    if "devicesList" in lista[0]:
        h.readDevice(f)

    
           
    return 


if __name__=="__main__":
    f=open("catalog.json")
    f.readline() ##first line is useless
    
    ##set owner
    line=f.readline()
    lista=line.split(':') 
    owner=parse(lista[1])

    ##set project name
    line = f.readline()
    lista=line.split(':')
    name=parse(lista[1])    

    ##set lastupdate
    line = f.readline()
    lista=line.split(':')
    update=parse(lista[1]+lista[2])
    
    p = Project(owner,name,update)

    print("Owner: ", p.getOwner())
    print("Project name: ", p.getName())
    print("Last update: ", p.getLastUpdate())

    line= f.readline()
    lista=line.split(':')
    
    if "usersList" in lista[0]:
        user=1
        while(user):
            line=f.readline()
            if '{' in line:
                readUser(f, p)
            elif "]," in line:
                user=0 #user are finished

    line= f.readline()
    lista=line.split(':')

    
    if "houses" in lista[0]:
        house=1
        while(house):
            line=f.readline()
            if '{' in line:
                readHouse(f,p)
            elif '],' in line:
                house=0
                
##        ##now i need to save Users
##        line=f.readline()
##        readUser(f, p)

    ##elif lista[0] == '"houses"' :
    print("Print users list")
    p.printUserList()
    print("Print houses list for each User")
    p.getHouseListOfEachUser()
    print("print all devices")
    p.showDeviceList()
    
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
