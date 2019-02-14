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
import ChatClient
import Message

# ------------------------------------------------------------#
# Server setting
Server_TCP_IP = '192.168.1.101'
Server_TCP_PORT = 8888
ChatClientArray = []
ChatMsgArray = []

# ------------------------------------------------------------#
# Server start
ChatRoom = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ChatRoom.bind((Server_TCP_IP, Server_TCP_PORT))
ChatRoom.listen(True)

def ThreadClient(CArray,client):
    CArray.append(client)

    while True:
        try:
            package = str(client.getClient().recv(1024))
            print package
            msg = package.split(",", 1)

            # true massage
            if msg[0] == client.getClientIP():
                ChatMsgArray.append(Message.Message(client.getClientIP(),msg[1]))
        except:
            print client.getClientIP() + 'Error'
            break
    client.setStatus(False)
    client.getClient().close()

def ChatRoomManger(CArray,MArray):
    while True:
        try:
            for i in range(CArray.__len__()):
                if not CArray[i].getStatus():
                    print 'ChatClient ' + CArray[i].getClientIP() + ' disConnect'
                    del CArray[i]
                    break

            if MArray.__len__() > 0:
                for i in range(CArray.__len__()):
                    if CArray[i].getStatus() and CArray[i].getClientIP() != MArray[0].getClientIP():
                        sendmsg = MArray[0].getClientIP() + ',' + MArray[0].getMsg()
                        CArray[i].getClient().send(sendmsg)
                del MArray[0]
        except:
            print 'ChatRoomManger error'

if __name__ == '__main__':
    print 'ChatRoom Server Start'

    # start Manager
    thread.start_new_thread(ChatRoomManger, (ChatClientArray,ChatMsgArray))

    while True:
        # connect to client
        try:
            client, addr = ChatRoom.accept()
            print 'Now connect client ip : ' + str(addr[0])

            # return ip
            client.send(str(addr[0]))
            NewClient = ChatClient.ChatClient(str(addr[0]),client)
            thread.start_new_thread(ThreadClient, (ChatClientArray, NewClient))
        except:
            break

print "server end"