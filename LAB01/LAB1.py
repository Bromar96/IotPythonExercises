###MAIN CLASS
from  Calculator import *
from  CalculatorExt import *

def printJSON(f,operation,a,b,c):
    f.write(f'\n\t"operation": "{operation}",')
    f.write(f'\n\t"operand_1": {a},')
    f.write(f'\n\t"operand_2": {b},')
    f.write(f'\n\t"result"   : {c} ')
    return

def printJSONext(f,operation,lista,res):
    k=0
    f.write(f'\n\t"operation": "{operation}",')
    f.write('\n\t"operands": [')
    while k< (len(lista)-1):
        f.write(f'{lista[k]},')
        k+=1
    f.write(f'{lista[k]}],')
    f.write(f'\n\t"result"   : {res} ')
    return

if __name__=="__main__":


    ##EXERCISE N 1
    print("EXERCISE 1")
    
    calc=Calculator()
    flag = 1
    print("We want to use a calculator")
    print("Available operations: add, sub, mul, div  (type 'exit' to finish)") 
    f=open("result.json", "w")
    f.write("{")
    i=0
    while(flag):
        oper=input('Insert operation: ')
        if oper == "exit":
            print('Finish')
            flag = 0
        else:
            op1=int(input('Insert operand1: '))
            op2=int(input('Insert operand2: '))
            result = calc.compute(oper,op1,op2)
            if result == "":
                print('Finish')
                flag = 0
            elif i==0:
                f.write(f'\n"operation{i}":')
                f.write(" {")
                printJSON(f,oper,op1,op2,result)
                f.write("\n}")
            else:
                f.write(f',\n"operation{i}":')
                f.write(" {")
                printJSON(f,oper,op1,op2,result)
                f.write("\n}")
        i+=1
    f.write("\n}") ##JSON file closed
    f.close()


    ##EXERCISE N 2
    print("EXERCISE 2")
    calcExt=CalculatorExt()
    flag = 1
    f2=open("result2.json", "w")
    f2.write("{")
    i=0
    print("Available operations: add, sub, mul, div  (type 'exit' to finish)")
    while(flag):
        oper=input('Insert operation: ')
        if oper == "exit":
            print('Finish')
            flag = 0
        else:
            operands=[]
            true=1
            print("Insert a list of operands")
            while true:
                new=input("\toperand: ")
                if new == "end":
                    true=0
                else:
                    operands.append(int(new))
                    
            result2 = calcExt.computeExt(oper,operands)
            ##  print('Result is: ', result)
            if result2 == "":
                print('Finish')
                flag = 0
            elif i==0:
                f2.write(f'\n"operation{i}":')
                f2.write(" {")
                printJSONext(f2,oper,operands,result2)
                f2.write("\n}")
            else:
                f2.write(f',\n"operation{i}":')
                f2.write(" {")
                printJSONext(f2,oper,operands,result2)
                f2.write("\n}")
        i+=1
    f2.write("\n}") ##JSON file closed
    f2.close()

    
