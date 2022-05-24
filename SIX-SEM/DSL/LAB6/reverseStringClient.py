import socket


IP = 'localhost'
PORT = 9598


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))
str1 = str(input("Enter the string : "))
clientSocket.send(str.encode(str1))
data = clientSocket.recv(1024)
data = data.decode()
print("The reversed string is sent by the server is = " + str(data))
clientSocket.close()