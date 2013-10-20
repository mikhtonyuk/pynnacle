from interfaces import IRouter
import urlparse
import threading


class RoundRobinRouter(IRouter):
    def __init__(self, *urls):
        self.urls = map(urlparse.urlparse, urls)
        self.robin = list(self.urls)
        self.lock = threading.Lock()

    def nodes(self):
        return self.urls

    def getRoutes(self, req):
        self.lock.acquire()
        try:
            ret = list(self.robin)
            t = self.robin[-1]
            self.robin[-1] = self.robin[0]
            self.robin[0] = t
            return ret
        finally:
            self.lock.release()
