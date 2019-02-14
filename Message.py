#!/usr/bin/python
# -*- coding: UTF-8 -*-
##
#
#   author  :   Chia Yuan Lin
#
#   email   :   lo919201@gmail.com
#
# #
class Message:

    def __init__(self,ip,msg):
        self.__ClientIP = ip    # Connect IP
        self.__Msg = msg        # Send Message

    def getClientIP(self):
        return self.__ClientIP
    def setClientIP(self, clientiP):
        self.__ClientIP = clientiP

    def getMsg(self):
        return self.__Msg
    def setMsg(self,msg):
        self.__Msg = msg
