from hk2.types import interface


@interface
class ICodec(object):
    def write(self, conn, msg):
        pass

    def read(self, conn):
        pass
