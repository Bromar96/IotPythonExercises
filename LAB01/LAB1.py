###MAIN CLASS
from  Calculator import *

if __name__=="__main__":
    
    calc=Calculator()
    flag = 1
    print("We want to use a calculator")
    print("Available operations: add, sub, mul, div  (tape 'exit' to finish)") 
    f=open("result.json", "w")
    f.write("{")
    while(flag):
        oper=input('Insert operation: ')
        if oper == "exit":
            print('Finish')
            flag = 0
        else:
            op1=int(input('Insert operand1: '))
            op2=int(input('Insert operand2: '))
            result = calc.compute(oper,op1,op2)
            if result == -1:
                print('Finish')
                flag = 0
            
            else:
                f.write(f'\n"operation": "{oper}",')
                f.write(f'\n"operand_1": "{op1}",')
                f.write(f'\n"operand_2": "{op2}"')
                print(f"The result is {result}")
    f.write("\n}")
    f.close()
##    print('Division is equal to', DIV)
    
