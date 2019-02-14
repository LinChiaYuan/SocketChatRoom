#!/usr/bin/python
# -*- coding: UTF-8 -*-
##
#
#   author  :   Chia Yuan Lin
#
#   email   :   lo919201@gmail.com
#
# #
class ChatClient:

    def __init__(self,ip,client):
        self.__ClientIP = ip    # Connect IP
        self.__Status = True   # Connect status
        self.__Client = client  # socket client

    def getClientIP(self):
        return self.__ClientIP
    def setClientIP(self, clientiP):
        self.__ClientIP = clientiP

    def getStatus(self):
        return self.__Status
    def setStatus(self,status):
        self.__Status = status

    def getClient(self):
        return self.__Client
    def setClient(self, client):
        self.__Client = client

