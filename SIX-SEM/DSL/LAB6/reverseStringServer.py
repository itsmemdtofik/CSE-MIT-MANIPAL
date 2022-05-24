import socket


IP = 'localhost'
PORT = 9598

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, PORT))
serverSocket.listen(1)

print("Now the server is ready to receive :-")
while 1:
	conn, addr = serverSocket.accept()
	print("Connected ...\n")
	data = conn.recv(1024)
	if not data:
		break
	data = data.decode()
	print("The data which is sent by client = " + str(data))
	str1 = str(data)
	str2 = str1[::-1]
	print("The server is going to sent the reversed string '" + str2 + "' to its client : \n")
	conn.send(str.encode(str2))
	conn.close()
