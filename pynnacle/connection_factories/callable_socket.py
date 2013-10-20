class CallableSocket(object):
    def __init__(self, clb):
        self.clb = clb
        self.buf = []

    def send(self, data):
        ret = self.clb(data)
        self.buf.append(ret)

    def recv(self, buflen):
        return self.buf.pop(0)