from interfaces import IRouter


class RouterTracer(IRouter):
    def __init__(self, router, tracer):
        self.router = router
        self.tracer = tracer

    @staticmethod
    def wrap(router, tracer):
        return router if tracer is None else RouterTracer(router, tracer)

    def getRoutes(self, req):
        with self.tracer.router_getRoutes(req) as t:
            ret = self.router.getRoutes(req)
            t.returned(ret)
            return ret
