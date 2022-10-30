#Import library so calls for library functions will work
from socket import*

#Assign the port number 12000 to the server application
serverPort = 12000

#Create a variable called serverSocket
#Using the python libraries call the socket function
#Add the arguments AF_INET and Sock_STREAM to the function
#AF_INET sets the the IP system to IPv4
#SOCK_STREAM sets the protocol to TCP
serverSocket = socket(AF_INET,SOCK_STREAM)

#This function associates this socket with the contents
#of the variable serverPort, in this case 12000
serverSocket.bind(('',serverPort))

#This function creates the welcoming door by telling the socket
#to start listening to port 12000
serverSocket.listen(1)

#This is a message printed to the terminal so we can tell the 
#server is started
print 'The server is listening'

#Infinite while loop so the server stays up and running
while 1:
	#This function receives the incoming connection request
	#and creates a new socket for this communication
	connectionSocket,addr = serverSocket.accept()

	#This variable accepts and holds the incoming message
	sentence = connectionSocket.recv(1024)

	#This function capitalizes the message
	capitalizedSentence = sentence.upper()

	#This function sends the modified message back to the
	#client
	connectionSocket.send(capitalizedSentence)

	#This function closes the TCP socket created by the incoming connection request
	connectionSocket.close()