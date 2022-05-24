import socket
clientSocket = socket.socket()
HOST = 'localhost'
PORT = 9172
print("Waiting for a connection : \n")
try:
    clientSocket.connect((HOST, PORT))
except socket.error as err:
    print(str(err))
response = clientSocket.recv(1024)
while True:
    msg = input("Client say something : \n")
    clientSocket.send(str.encode(msg))
    response = clientSocket.recv(1024)
    print('From server : ', +response.decode())
clientSocket.close()
