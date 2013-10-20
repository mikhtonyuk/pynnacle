from interfaces import IConnectionFactory
from callable_socket import CallableSocket


class CallableConnectionFactory(IConnectionFactory):
    def __init__(self):
        self.fail = False

    def get(self, url):
        return CallableSocket(lambda data: self.onSend(url, data))

    def release(self, conn):
        pass

    def onSend(self, url, data):
        if self.fail:
            raise Exception("fake socket error")
        return "echo: {}".format(data)