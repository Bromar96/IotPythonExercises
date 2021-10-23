##Main class

class Calculator:
    def compute(self,operation,a,b):
        res = 0
        if operation == "add":
            res = self.add(a,b)
        elif operation == "sub":
            res = self.sub(a,b)
        elif operation == "mul":
            res = self.mult(a,b)
        elif operation == "div":
            try:
                res = self.div(a,b)
            except:
                print("DivException occurred")
                res=-1
        else:
            print("Not valid operation!")
            res = -1
        return res
    
    def add(self, a, b):
        return a+b
    def sub(self, a, b ):
        return a-b
    def mult(self, a, b):
        return a*b
    def div(self, a, b):
        if b == 0:
            raise ValueError("Dividen can't be equal to zero ")
        else:
            return a/b
        
    
