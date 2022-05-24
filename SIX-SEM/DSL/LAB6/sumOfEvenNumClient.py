import socket

IP = 'localhost'
PORT = 9598

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((IP, PORT))

data = str(input("Enter the number to send to server : "))
clientSocket.send(str.encode(data))

data = clientSocket.recv(1024)
data = data.decode()
temp = [float(x) for x in data.split(' ')]
print("The sum of even  number which is sent bt server is = " + str(temp[0]))
clientSocket.close()

