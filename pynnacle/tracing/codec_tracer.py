from interfaces import ICodec


class CodecTracer(ICodec):
    def __init__(self, codec, tracer):
        self.codec = codec
        self.tracer = tracer

    @staticmethod
    def wrap(codec, tracer):
        return codec if tracer is None else CodecTracer(codec, tracer)

    def write(self, conn, msg):
        with self.tracer.codec_write(conn, msg):
            self.codec.write(conn, msg)

    def read(self, conn):
        with self.tracer.codec_read(conn) as r:
            msg = self.codec.read(conn)
            r.returned(msg)
            return msg
