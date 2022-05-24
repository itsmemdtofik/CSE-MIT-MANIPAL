import socket

IP = 'localhost'
PORT = 1234

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((IP, PORT))
serverSocket.listen(1)
print("The server is ready to recieve : \n")
while 1:
	conn, addr = serverSocket.accept()
	print("Connected....\n")
	data = conn.recv(1024)
	if not data:
		break
	data = data.decode()
	print("The number which the client sent = " + data)
	reverseNumber = 0
	num = int(data)
	while(num > 0):
		rem = num % 10
		reverseNumber = reverseNumber * 10 + rem
		num = num // 10
	msg = str(reverseNumber)
	print("Now the server is going to send this reversed number -> " + msg + " to its client")
	conn.send(str.encode(msg))
	conn.close()
