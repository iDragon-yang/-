from socket import *
import random


class server():
    def __init__(self,my_id,friend_id):
        self.my_id=my_id
        self.friend_id=friend_id
        #self.serverName = '192.168.8.100'
        self.serverName='192.168.43.146'
        self.serverPort = 12000
        self.clientPort=random.randint(10000,20000)
        self.if_first=True
        self.clientSocket = socket(AF_INET,SOCK_DGRAM)
        self.clientSocket.bind(('',self.clientPort))
        self.first_connect()
        self.newmessage=['']

    def first_connect(self):
        self.clientSocket.sendto(('@'+str(self.my_id)).encode(),(self.serverName,self.serverPort))
        self.if_first=False
        return

    def sendMessage(self,message):
        self.clientSocket.sendto((message+'@'+str(self.friend_id)).encode(),(self.serverName,self.serverPort))
        return

    def receive_message(self):
        while 1:
            print('i am ready')
            modifiedMessage,Severaddress=self.clientSocket.recvfrom(2048)
            self.newmessage.append(modifiedMessage.decode())
            print(self.newmessage)
        