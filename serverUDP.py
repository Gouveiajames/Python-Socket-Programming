#Import library so calls for library functions will work
from socket import*

#Assign the port number 12000 to the server application
serverPort = 12000

#Create a variable called serverSocket
#Using the python libraries call the socket function
#Add the arguments AF_INET and Sock_DGRAM to the function
#AF_INET sets the the IP system to IPv4
#SOCK_DGRAM sets the protocol to UDP
serverSocket = socket(AF_INET,SOCK_DGRAM)

#This function associates this socket with the contents
#of the variable serverPort, in this case 12000
serverSocket.bind(('',serverPort))

#This is a message printed to the terminal so we can tell the 
#server is started
print 'The server is listening'

#Infinite while loop so the server stays up and running
while 1:
	#The sentence variable accepts and holds the incoming message
	#The clientAddress variable holds the clients address
	sentence, clientAddress = serverSocket.recvfrom(1024)

	#This function capitalizes the message
	capitalizedSentence = sentence.upper()

	#The arguments capitalizedSentence and client Address are 
	#passed into the send function thus sending the modified
	#message back to the client.
	serverSocket.sendto(capitalizedSentence, clientAddress)