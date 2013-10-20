from interfaces import IRouter
import urlparse


class FailoverRouter(IRouter):
    def __init__(self, *urls):
        self.urls = map(urlparse.urlparse, urls)

    def nodes(self):
        return list(self.urls)

    def getRoutes(self, req):
        return list(self.urls)
