import json
from MyMQTT import *

class DataCollector:
    def __init__(self,clientID,broker,baseTopic):
        self.clientID=clientID
        self.baseTopic=baseTopic
        self.client=MyMQTT(clientID,broker,1883,self)
	
    def run(self):
        self.client.start()
        print('{} has started'.format(self.clientID))

    def end(self):
        self.client.stop()
        print('{} has stopped'.format(self.clientID))

    def follow(self, newTopic):
        self.client.unsubscribe()
        #fp = open("topic.txt","r")
        #topic = fp.readline()
        #fp.close()
        self.client.mySubscribe(newTopic)

    def notify(self,topic,msg):
        payload=json.loads(msg)
        #print(json.dumps(payload, indent=4))
        json.dump(payload,open("catalog.json", "w"))

    def setup(self):
        #fp = open("topic.txt","w")
        #fp.write(self.baseTopic)
        #fp.close()
        self.client.mySubscribe(self.baseTopic)
