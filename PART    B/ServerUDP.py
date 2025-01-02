from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))

print("The server is ready to receive")

while 1:
    sentence, clientAddress = serverSocket.recvfrom(2048)
    sentence = sentence.decode("utf-8")
    
    try:
        with open(sentence, "r") as file:
            con = file.read(2048)
        serverSocket.sendto(bytes(con, "utf-8"), clientAddress)
        print('\nSent contents of', sentence)
    except FileNotFoundError:
        error_msg = "Error: File not found"
        serverSocket.sendto(bytes(error_msg, "utf-8"), clientAddress)
        print("File not found:", sentence)
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        serverSocket.sendto(bytes(error_msg, "utf-8"), clientAddress)
        print("Error:", str(e))

