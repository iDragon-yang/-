from socket import *
serverPort=12000

#clientName = '192.168.8.100'
clientName='192.168.43.146'


serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print("The server is ready to receive")
address_dict={}

while 1:
	message,clientAddress=serverSocket.recvfrom(2048)
	message=message.decode()
	print(message,'from',clientAddress)
	if(message[0]=='@'):
			#传送自己的id与地址
			address_dict[message.split('@')[1]]=clientAddress[1]
			print(address_dict)
	else:
			#第一个为所发送信息，第二个是接收者id
			print('i have sent')
			serverSocket.sendto(message.encode(),(clientName,address_dict[message.split('@')[1].split('\n')[0]]))
