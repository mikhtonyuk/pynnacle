from interfaces import IConnectionFactory
import socket


class SocketConnectionFactory(IConnectionFactory):
    def get(self, url):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((url.hostname, url.port))
        return sock

    def release(self, conn):
        conn.close()
