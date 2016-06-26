# Socket-Assignment

import socket  # Import socket module
from thread import *

s = socket.socket()
HOST = ''
port = 5178  # Reserve a port for your service.

s.connect((HOST, port))
print s.recv(1024)

data=raw_input("Your Name: ")
s.send(data)
second=raw_input("Chat with: ")
s.send(second)
def receive():
    while True:
        data=s.recv(1024)
        print data

start_new_thread(receive, (s,))
while 1:
    rep=raw_input()
    if rep=='q':
        s.send(rep)
        break
    else:
        s.send(rep)




s.close
