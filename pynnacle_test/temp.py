from routers import *
from connection_factories.callable import CallableConnectionFactory
from codecs.text import TextCodec
from tracing import *
from service import Service

import urlparse

#----------------------------------------------------------


class LoggingTrace(NullTracer):
    def router_getRoutes(self, req):
        t = OpTracer()
        t.onReturn = self.onRoute
        return t

    def connectionFactory_get(self, url):
        print "  connect: {}".format(url.geturl())
        return self.nullTrace

    def connectionFactory_release(self, conn):
        print "  disconnect"
        return self.nullTrace

    def codec_write(self, conn, msg):
        print "    write: {}".format(msg)
        return self.nullTrace

    def codec_read(self, conn):
        t = OpTracer()
        t.onReturn = self.onRead
        return t

    def service_request(self, req):
        print "REQ:  {}".format(req)
        t = OpTracer()
        t.onReturn = self.onResponse
        t.onError = self.onError
        return t

    def onRoute(self, routes):
        print "  routes: {}".format(', '.join(map(urlparse.urlunparse, routes)))

    def onRead(self, data):
        print "    read: {}".format(data)

    def onResponse(self, resp):
        print "RESP: {}".format(resp)

    def onError(self, exc_type, exc_val, exc_tb):
        print "ERR:  {}".format(exc_val)

#----------------------------------------------------------

if __name__ == '__main__':
    codec = TextCodec()
    conn = CallableConnectionFactory()
    router = FailoverRouter("clb://127.0.0.1:8001", "clb://127.0.0.1:8002")

    tracer = LoggingTrace()

    svc = ServiceTracer(
        Service(codec, conn, router, tracer),
        tracer)

    svc.request("#yolo1")

    conn.fail = True
    try:
        svc.request("#yolo2")
    except Exception as ex:
        pass

    conn.fail = False
    svc.request("#yolo3")
