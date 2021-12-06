import json
import requests

if __name__ == '__main__':
    print("LAB 3 Exercise 1\n\n")
    print("We want to use a calculator")
    print("Available operations: add, sub, mul, div  (type 'exit' to finish)")
    oper=input('Insert operation: ')
    if(oper == 'add' or oper == 'sub' or oper == 'mul' or oper == 'div'):
        op1=input('Insert operand1: ')
        op2=input('Insert operand2: ')
        payload = {'op1': op1, 'op2': op2}
        
        req = requests.get("http://localhost:8080/"+oper, params=payload)
        #print(req)
        #r = requests.get("http://localhost:8080/add?op1=2&op2=3")
        print(req.url)
        y=json.dumps(req.json())  #y is a string
        myDict = json.loads(y) 
        print("operation:      "+myDict['operation'])
        print("first operand:  "+str(myDict['operand_1']))
        print("second operand: "+str(myDict['operand_2']))
        print("result:         "+str(myDict['result']))
        print("OK")
    else:
        print("Operation not valid")

