from hk2.types import interface


@interface
class ITracer(object):
    def codec_write(self, conn, msg):
        pass

    def codec_read(self, conn):
        pass

    def connectionFactory_get(self, url):
        pass

    def connectionFactory_release(self, conn):
        pass

    def router_getRoutes(self, req):
        pass

    def service_request(self, req):
        pass


class NullTrace(object):
    def __enter__(self):
        return self

    def returned(self, value):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False


class OpTracer(object):
    def __init__(self):
        self.onEnter = None
        self.onReturn = None
        self.onError = None

    def __enter__(self, *vargs, **kwargs):
        if self.onEnter:
            self.onEnter(*vargs, **kwargs)
        return self

    def returned(self, value):
        if self.onReturn:
            self.onReturn(value)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val and self.onError:
            self.onError(exc_type, exc_val, exc_tb)


class NullTracer(ITracer):
    nullTrace = NullTrace()

    def codec_write(self, conn, msg):
        return self.nullTrace

    def codec_read(self, conn):
        return self.nullTrace

    def connectionFactory_get(self, url):
        return self.nullTrace

    def connectionFactory_release(self, conn):
        return self.nullTrace

    def router_getRoutes(self, req):
        return self.nullTrace

    def service_request(self, req):
        return self.nullTrace
