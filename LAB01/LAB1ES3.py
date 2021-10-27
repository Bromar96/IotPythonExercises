## MAIN CLASS
from Project import *
from User import *
from House import *

##given a line of a json file "key": "value", returns only value
def searchValue(stringa):
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

    p.createUser(name,userID,chatID)
    
    
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
    if lista[0] == '  "usersList"':
        ##now i need to save Users
        line=f.readline()
        print("sono qui")
        readUser(f, p)

    ##elif lista[0] == '"houses"' :

    
    
##    print(p.getUserList())
##    print(p.getHouseList())
##    h = House(24,1)
##
##    p.addToHouseList(h)
##    
##    newHouse = p.getHouseList().pop()
##
##    print(newHouse.getUserID())


##second approach: read one line and consider it as a pair "key":"value"
    line=f.readline()
    name=searchValue(line)
    line=f.readline()
    update=searchValue(line)
    
    ##if(line= "}"):
    f.close()
    print("End of file")
