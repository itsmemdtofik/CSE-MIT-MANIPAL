import socket
import os
from _thread import *
serverSocket = socket.socket()
HOST = 'localhost'
PORT = 9172
threadCount = 0
try:
    serverSocket.bind((HOST, PORT))
except socket.error as err:
    print(str(err))
print("Waiting for a connection : \n")
serverSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the server'))
    while True:
        data = connection.recv(2048)
        print('Recieved from client : ' + str(threadCount) + data.decode())
        msg = input("Server says : \n")
        if not data:
            connection.sendall(msg.encode())
    connection.close()
    while True:
        clientConn, clientAddr = serverSocket.accept()
        print('Connected to : ', +clientAddr[0] + ':'+str(clientAddr[1]))
        start_new_thread(treaded_client, ((clientConn, )))
        threadCount += 1
        print("Thread number : \n")
    serverSocket()
