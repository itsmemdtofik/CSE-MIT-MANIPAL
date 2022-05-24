import socket
serverIP = 'localhost'
serverPORT = 1515
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverIP, serverPORT))
message1 = str(input("Input integer with space between : "))
message2 = str(input("Enter the length of the set : "))
clientSocket.send(str.encode(message1))
data = clientSocket.recv(1024)
data = data.decode()
temp = [float(x) for x in data.split(' ')]
print("The total of all numbers is = " + str(temp[0]))
print("The lowest number is = " + str(temp[1]))
print("The highest number  is = " + str(temp[2]))
print("The mean is = " + str(temp[3]))
clientSocket.close()
