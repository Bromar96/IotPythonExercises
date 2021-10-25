#Extension of class Calculator
from Calculator import * 

class CalculatorExt(Calculator):
    def computeExt(self,operation,lista):
        finalRes=""
        res=0

        for i in lista:
            if operation == "add":
                res = Calculator.add(self,res,i)
            elif operation == "sub":
                if res==0:
                    res = Calculator.add(self,res,i)  ##first operand must be ADDED 
                else:
                    res = Calculator.sub(self,res,i)
            elif operation == "mul":
                if res==0:
                    res = Calculator.add(self,res,i)  ##first operand must be ADDED 
                else:
                    res = Calculator.mult(self,res,i)
            elif operation == "div":
                if res==0:
                    res = Calculator.add(self,res,i)  ##first operand must be ADDED 
                else:
                    try:
                        res = Calculator.div(self,res,i)
                    except:
                        print("DivException occurred")
                        res = ""
            else:
                print("Not valid operation!")
                res = ""
        finalRes = str(res)
        return finalRes

        
    
