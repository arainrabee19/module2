import socket  # Import socket module
from thread import *
import sys



host = socket.gethostname()
buffer=2048
port = 5005  # Reserve a port for your service.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(10)
print s.recv(1024)

c=[]

c.append(s)

print "Chat server started on port " + str(port)


def receive():
    while True:
        data=s.recv(1024)
        print data

start_new_thread(receive, ())
while 1:
    name=raw_input('your name: ')
    s.send(name)
    name=raw_input('second user name: ')
    s.send(name)

while True:
    data=raw_input('Me bola hun: ')
    s.send(data)


s.close()
