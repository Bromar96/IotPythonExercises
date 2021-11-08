###MAIN CLASS
import cherrypy
import json
from Calculator import *



class myWebService:
    
    exposed = True

    def __init__(self):
        pass
    
    def GET(self,*uri,**params):  ##uri is the operation, params are the operands
        calc=Calculator()
        f=open("result.json", "w")
        f.write("{")
        toReturn=""
        myOperation={}
        if len(uri)!=0:
            oper = uri[0]
            op1=int(params["op1"])
            op2=int(params["op2"])
            result = calc.compute(oper,op1,op2)
            if result=="":
                self.operationFailed(f)
                f.close()
                return "OperationFailed"
            else:
                self.printJSON(f,oper,op1,op2,result)
                #json.dump(myOperation,f,indent=4)
        myOperation={"operation": oper, "operand_1": op1,"operand_2": op2, "result": result}
      
        f.write("\n}") ##JSON file closed
        f.close()        
        return  json.dumps(myOperation)  

    def printJSON(self,f,operation,a,b,c):
        f.write(f'\n\t"operation": "{operation}",')
        f.write(f'\n\t"operand_1": {a},')
        f.write(f'\n\t"operand_2": {b},')
        f.write(f'\n\t"result"   : {c} ')
        
        return

    def operationFailed(self,f):
         f.write(f'\n\t"operation": "failed",')
         return
if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(myWebService(), '/', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()

    

    
