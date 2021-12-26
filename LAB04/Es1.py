##LAB 4 exercise 1

import cherrypy
import json
from MyMQTT import *
from DataCollector import *

class myWebService:

    exposed = True

    def __init__(self):
        pass

    def GET(self,*uri):
        if uri[0] == "temperature":
            coll
        elif uri[0] == "humidity":
            return "hum"
        elif uri[0] == "allSensor":
            return "sens"
        
if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    config = json.load(open("settings.json"))
    coll = DataCollector('OG303030',config["broker"],config["baseTopic"])
    coll.run()
    cherrypy.tree.mount(myWebService(), '/', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()
