import cherrypy

class HelloWorld:
	exposed=True
	def GET(self,*uri,**params):
		output = "Hello World!\n"
		output+=str(uri)+"\n"
		output+=str(params)+"\n"
		return output

if __name__=="__main__":
	conf={
		'/':{
			'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
			'tools.sessions.on':True,
		}
	}
	cherrypy.tree.mount(HelloWorld(),'/',conf)
	cherrypy.config.update(conf)
	cherrypy.engine.start()
	cherrypy.engine.block()
