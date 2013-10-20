from interfaces import IService
from tracing import CodecTracer, ConnectionFactoryTracer, RouterTracer


class Service(IService):
    def __init__(self, codec, connFactory, router, tracer=None):
        self.codec = CodecTracer.wrap(codec, tracer)
        self.connFactory = ConnectionFactoryTracer.wrap(connFactory, tracer)
        self.router = RouterTracer.wrap(router, tracer)
        self.tracer = tracer

    def request(self, req):
        urls = self.router.getRoutes(req)
        conn = self.connFactory.get(urls[0])
        try:
            self.codec.write(conn, req)
            resp = self.codec.read(conn)
            return resp
        finally:
            self.connFactory.release(conn)
