from interfaces import ICodec


class TextCodec(ICodec):
    def write(self, conn, msg):
        conn.send(msg)

    def read(self, conn):
        return conn.recv(4096)
