from interfaces import IService


class RetryFilter(IService):
    def __init__(self, svc, retries):
        self.svc = svc
        self.retries = retries

    def request(self, req):
        tries = self.retries
        while True:
            try:
                tries -= 1
                return self.svc.request(req)
            except:
                if tries <= 0:
                    raise
