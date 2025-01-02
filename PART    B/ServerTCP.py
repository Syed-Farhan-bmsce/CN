from socket import *

serverName = "127.0.0.1"
serverPort = 12000

# Create the server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the server to the specified address and port
serverSocket.bind((serverName, serverPort))

# Start listening for client connections
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    # Accept a connection from the client
    connectionSocket, addr = serverSocket.accept()
    
    # Receive the file name from the client
    sentence = connectionSocket.recv(1024).decode()
    
    # Open the file
    try:
        with open(sentence, 'r') as file:
            # Read the file contents
            fileContents = file.read(1024)
            # Send the file contents back to the client
            connectionSocket.send(fileContents.encode())
            print(f"\nSent contents of {sentence}")
    except FileNotFoundError:
        # If the file is not found, send an error message
        connectionSocket.send(b"File not found.")

    # Close the connection with the client
    connectionSocket.close()
