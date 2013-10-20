from hk2.types import interface


@interface
class IRouter(object):
    def nodes(self):
        """ Returns all available nodes for routing """

    def getRoutes(self, req):
        """ Returns list of nodes in prioritized order """
