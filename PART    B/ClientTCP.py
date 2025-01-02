from socket import *

serverName = '127.0.0.1'
serverPort = 12000

# Create a socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Get the file name from the user
sentence = input("\nEnter file name: ")

# Send the file name to the server
clientSocket.send(sentence.encode())

# Receive the file contents from the server
filecontents = clientSocket.recv(1024).decode()

# Print the contents received from the server
print('\nFrom Server:\n')
print(filecontents)

# Close the socket connection
clientSocket.close()
