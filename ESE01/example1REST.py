##REST EXAMPLE 1

import random
import string
import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def generate(self,length=8):
        return ''.join(random.sample(string.hexdigits,int(length)))
    
    @cherrypy.expose
    def myMethod(self):
        return "Provaaaa!"

    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def display(self):
        cherrypy.session['mystring'] = "Ciao a tutti"
        return cherrypy.session['mystring']

if __name__=="__main__":
    conf = {
        '/': {'tools.sessions.on':True
              }
        }
    cherrypy.tree.mount(StringGenerator(),'/',conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
