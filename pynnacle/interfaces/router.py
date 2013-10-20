from hk2.types import interface


@interface
class IRouter(object):
    def getRoutes(self, req):
        pass
