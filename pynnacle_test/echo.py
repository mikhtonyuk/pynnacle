import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(('127.0.0.1', 8888))
srv.listen(1)
print "Listening..."

cl, addr = srv.accept()
print "Accepted connection: {}".format(addr)

while True:
    read = cl.recv(4098)
    if not read:
        break

    cl.sendall("echo: " + read)