#Import library so calls for library functions will work
from socket import*

#Set the variable serverName to contain the ip address of the server
#in this case it corresponds to a windows machine on my wifi
serverName = '192.168.1.69'

#Set the variable serverPort to contain the port number where
#the server is listening
serverPort = 12000

#create a variable called clientSocket
#Using the python libraries call the socket function
#Add the arguments AF_INET and Sock_STREAM to the function
#AF_INET sets the the IP system to IPv4
#SOCK_STREAM sets the protocol to TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

#This function creates the TCP connection to the server
#ServerName sets the IP address of the server
#serverPort sets the port number of the server application
clientSocket.connect((serverName, serverPort))

#This variable holds the input from the user
sentence = raw_input('Input lower case sentence:')

#This function sends the input from the user to the server
clientSocket.send(sentence)

#This variable holds the sentence returned from the server
modifiedSentence = clientSocket.recv(1024)

#Print the returned sentence to the terminal
print 'From server:', modifiedSentence

#Close the TCP socket
clientSocket.close()