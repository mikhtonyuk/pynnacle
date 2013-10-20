from interfaces import IRouter
import urlparse


class RoundRobinRouter(IRouter):
    def __init__(self, *urls):
        self.urls = map(urlparse.urlparse, urls)
        self.current = 0

    def getRoutes(self, req):
        ret = list(self.urls)
        t = self.urls[-1]
        self.urls[-1] = self.urls[0]
        self.urls[0] = t
        return ret
