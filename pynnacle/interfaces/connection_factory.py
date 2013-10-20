from hk2.types import interface


@interface
class IConnectionFactory(object):
    def get(self, url):
        pass

    def release(self, conn):
        pass
