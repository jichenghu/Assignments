from socket import *

serverPort = 10086
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print ('The server is ready')

while True:
    connectionSocket, addr = serverSocket.accept()

    number = int(connectionSocket.recv(1024).decode())
    result = 0

    for i in range(number + 1):
        result += i

    connectionSocket.send(str(result).encode())

    connectionSocket.close()