#!/usr/bin/python
# -*- coding: UTF-8 -*-
##
#
#   author  :   Chia Yuan Lin
#
#   email   :   lo919201@gmail.com
#
# #
import socket
import thread

# ------------------------------------------------------------#
# Server setting
Server_TCP_IP = '192.168.1.101'
Server_TCP_PORT = 8888
clientsocket=socket.socket()

# ------------------------------------------------------------#
# construct connect
def connectServer(IP, PORT):
    clientsocket.connect((IP, PORT))

def SendThread(Server,):
    while True:
        InputStr = raw_input()
        print '\n' + str(ip) + ' => ' + InputStr
        Server.send(str(ip) + ',' + InputStr)


# -------------------------------------------#
# Client start
if __name__ == "__main__":
    # Connect to Server
    connectServer(Server_TCP_IP, Server_TCP_PORT)
    ip = clientsocket.recv(1024)

    # Send Thread
    t = thread.start_new_thread(SendThread, (clientsocket,))

    # Read Server Msg
    while True:
        try:
            package = str(clientsocket.recv(1024))
            if package != '':
                msg = package.split(",", 1)
                if msg.__len__() == 2:
                    print msg[0] + " => " + msg[1]
        except:
            print "client end"
            break
            
clientsocket.close()