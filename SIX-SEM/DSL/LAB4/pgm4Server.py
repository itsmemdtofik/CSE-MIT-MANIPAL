import socket
serverIP = 'localhost'
serverPORT = 1515
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIP, serverPORT))
serverSocket.listen(1)
print("TCP server has started and ready to recieve : ")

while 1:
    connection, addr = serverSocket.accept()
    print("connected...\n")
    data = connection.recv(1024)
    if not data:
        break
    data = data.decode()
    print(data)
    temp = [float(x) for x in data.split(' ')]
    print("Received data : ", temp)
    length = len(temp)
    maximum = max(temp)
    minimum = min(temp)
    total = sum(temp)
    mean = total / length
    msg = str(total) + " " + str(minimum) + " " + str(maximum) + " " + str(mean)
    connection.send(str.encode(msg))
