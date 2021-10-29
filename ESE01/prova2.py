import cherrypy
class ParamsReverser():
    """docstring for Reverser"""

    exposed = True

    def __init__(self):
        pass

    def GET(self, *uri, **params):
        
        if len(uri) == 0:
            reverse={}
            for k in params.keys():
                reverse[k]=params[k][::-1]
            return json.dumps(reverse)
        else:
            raise cherrypy.HTTPError(400, 'No URI given, you need to provide at least one uri')

        
            

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(ParamsReverser(), '/simple', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
