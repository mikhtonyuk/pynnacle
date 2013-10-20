from hk2.types import interface


@interface
class IService(object):
    def request(self, req):
        pass
