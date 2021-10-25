##EXERCISE 1

import cherrypy

class MyWebService():
    exposed=True
    def GET(self,*uri):
        stringa=uri
        i=len(stringa)
        k=0
        while(i>=0):
            rev[k]=stringa[i]
            i-=1
            k+=1
        output=rev
        return output5

if __name__ == '__main__':
    conf={
        '/':{
                'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on':True
        }
    }
    cherrypy.tree.mount(MyWebService(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
    
