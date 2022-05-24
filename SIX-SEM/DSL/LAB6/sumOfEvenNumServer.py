import socket

IP = 'localhost'
PORT = 9598

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, PORT))
serverSocket.listen(1)

print("The server is ready to receive the data : \n")
while 1:
	conn, addr = serverSocket.accept()
	print("Connected...\n")
	data = conn.recv(1024)
	if not data:
		break
	data = data.decode()
	temp = [float(x) for x in data.split(' ')]
	print("The data which is sent by the client is = " + str(temp))
	summmation = 0
	for i in temp:
		if i % 2 == 0:
			summmation = summmation + i
	msg = str(summmation)
	conn.send(str.encode(msg))
	conn.close()



