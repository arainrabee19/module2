'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5178  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Start listening on socket
s.listen(10)
print 'Socket now listening'

add=[]
# Function for handling connections. This will be used to create threads

def chatlist(conn):
    y=1
    conn.send("available users")
    loop = len(add)
    while loop:
        loop=loop-1
        if add[loop]['conn']!=conn:
            conn.send(str(y)+':'+add[loop]['name']+"\n")
    return


def clientthread(conn):
    # Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n')  # send only takes string

    # infinite loop so that function do not terminate and thread do not end.
    x=-1
    while True:
        y=-1
        for data in range(len(add)):
            if add[x]['conn']==conn:
                x=data
                break
        data1 = conn.recv(1024)
        if data1=='q':
            Disconnect(add[data])
            print 'disconneected with ' + add[x]['address'][0]+' : '+str(add[x]['address'][0])
            del add[x]
            break
        else:
            y=-1
            to,reply=data.split(':',1)
            print to
            for data in range(len(add)):
                print add['name']
                if to==add[data]['name']:
                    y = data
                    break
            if y>-1:
                add[y]['conn'].send(to + ':' + reply)
            else:
                add[x]['conn'].send('user not available')
    conn.close()


def Disconnect(var):
    loop=len(add)
    while loop:
        loop=loop-1
        add[loop]['conn'].send("\n" + var['name'] + " is Offline. \n")
    return

def Connect(var):
    loop=len(add)
    while loop:
        loop=loop-1
        add[loop]['conn'].send("\n" + var['name'] + " is Online. \n")
    return




i=0
# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call

    conn, addr = s.accept()

    var={}
    var['conn']=conn
    var['address']=addr
    var['name']=conn.recv(100)
    Connect(var)
    add=add+[var]
    chatlist(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (add[i],))
    i+=1
s.close()
