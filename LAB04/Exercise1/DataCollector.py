import json
from MyMQTT import *

class DataCollector:

    def __init__(self,clientID,broker,baseTopic):
		self.clientID=clientID
		self.baseTopic=baseTopic
		self.client=MyMQTT(clientID,broker,1883, self)
	def run(self):
		self.client.start()
		print('{} has started'.format(self.clientID))
	def end(self):
		self.client.stop()
		print('{} has stopped'.format(self.clientID))
	def follow(self,topic):
		self.client.mySubscribe(topic)
	def notify(self,topic,msg):
		payload=json.loads(msg)
		print(json.dumps(payload,indent=4))
