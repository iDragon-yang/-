from socket import *
import random

serverName = '192.168.8.100'
serverPort = 12000
clientPort=random.randint(10000,20000)
def send(message):
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    clientSocket.bind(('',clientPort))
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
    #clientSocket.close()
    print(modifiedMessage.decode())

def first_connect(id):
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    clientSocket.bind(('',clientPort))
    clientSocket.sendto(('@'+id).encode(),(serverName,serverPort))

    
   
   


