import socket
IP = 'localhost'
PORT = 1234

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))
num1 = str(input("Enter the number : "))
clientSocket.send(str.encode(num1))
data = clientSocket.recv(1024)
data = data.decode()
print("The reversed number by the server is = " + str(data))
clientSocket.close()
