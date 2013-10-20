from interfaces import IService


class ServiceTracer(IService):
    def __init__(self, service, tracer):
        self.service = service
        self.tracer = tracer

    @staticmethod
    def wrap(service, tracer):
        return service if tracer is None else ServiceTracer(service, tracer)

    def request(self, req):
        with self.tracer.service_request(req) as t:
            resp = self.service.request(req)
            t.returned(resp)
            return resp
