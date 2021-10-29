import cherrypy
class UriReverser():
    """docstring for Reverser"""

    exposed = True

    def __init__(self):
        pass

    def GET(self, *uri):
        print(len(uri))
        if len(uri)>0:
            for x in uri:
                x=x[::-1]
            return ''.join(x)
        else:
            # you can define a simple http error message
            raise cherrypy.HTTPError(400, 'No URI given, you need to provide at least one uri')
            

if __name__ == '__main__':
    conf = {
        '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tool.session.on': True
        }
    }
    cherrypy.tree.mount(UriReverser(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
