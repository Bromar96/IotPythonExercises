##LAB 4 exercise 1

import cherrypy
import json
from MyMQTT import *
from DataCollector import *
import time

class myWebService:
    exposed = True

    def __init__(self, collector):
        self.dataColl = collector
        pass

    def GET(self,*uri):
        
        message={}
        if uri[0] == "temperature":
            message=self.getMessage(0)
            return json.dumps(message,indent=4) 
        elif uri[0] == "humidity":
            message = self.getMessage(1)
            return json.dumps(message,indent=4)
        elif uri[0] == "allSensor":
            message = self.getMessage(2)
            return json.dumps(message,indent=4)
        return "Welcome to my REST web page\nYou can use as URI /temperature, /humidity, /allSensor "

    def getMessage(self, param):
        #fp = open("topic.txt","w")
        if param == 2:
            topic="IoT_project/#"
        else:
            topic="IoT_project/0/1/0"
        #fp.write(topic)
        #fp.close()
        self.dataColl.follow(topic)
        time.sleep(10)
        msg=json.load(open("catalog.json", "r"))
        sID=msg['bn']
        diz = {}
        if param == 2:
            print(f"Topic {topic}")
            print(json.dumps(msg,indent=4))
            return msg
        else:
            diz['bn']= "Sensor"+str(sID)
            diz['e']=msg['e'][param]
            return diz
        
if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    config = json.load(open("settings.json"))
    coll = DataCollector('1234',config["broker"],config["baseTopic"])
    coll.setup()
    coll.run()
    time.sleep(10)
    cherrypy.tree.mount(myWebService(coll), '/', conf)
    # this is needed if you want to have the custom error page
    # cherrypy.config.update({'error_page.400': error_page_400})
    cherrypy.engine.start()
    cherrypy.engine.block()
