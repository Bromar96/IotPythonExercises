from Project import *

if __name__=="__main__":
    p = Project("Omar","myProj",'2020-2-27 14:06')

    print(p.getOwner())
    print(p.getName())
    print(p.getLastUpdate())
    print(p.getUserList())
    print(p.getHouseList())


