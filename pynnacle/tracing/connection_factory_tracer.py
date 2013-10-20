from interfaces import IConnectionFactory


class ConnectionFactoryTracer(IConnectionFactory):
    def __init__(self, connFactory, tracer):
        self.connFactory = connFactory
        self.tracer = tracer

    @staticmethod
    def wrap(connFactory, tracer):
        return connFactory if tracer is None else ConnectionFactoryTracer(connFactory, tracer)

    def get(self, url):
        with self.tracer.connectionFactory_get(url) as t:
            conn = self.connFactory.get(url)
            t.returned(conn)
            return conn

    def release(self, conn):
        with self.tracer.connectionFactory_release(conn):
            self.connFactory.release(conn)
