from socket import *

serverName = 'localhost'
serverPort = 10086

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

number = input('Please input a upper limit for accumulation from 1\n')
clientSocket.send(number.encode())

result = clientSocket.recv(1024).decode()
print('The result calculated by server is: ', result)

clientSocket.close()