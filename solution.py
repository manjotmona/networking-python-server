#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('127.0.0.1',13331))
serverSocket.listen(1)
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n'.encode())
        connectionSocket.send('\n HTTP 404 Not Found Error\n'.encode())
        connectionSocket.close()
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 