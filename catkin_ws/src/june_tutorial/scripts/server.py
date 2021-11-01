import socket

localIP="127.0.01"
localPort=9999
bufferSize=1024

UDPServerSocket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server listening")

while(True):
	bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
	message=bytesAddressPair[0]
	address=bytesAddressPair[1]

	clientMsg="Message from Client: {}".format(message.decode())
	clientIP="Client IP Address: {}".format(address)

	print(clientMsg)
	print(clientIP)

