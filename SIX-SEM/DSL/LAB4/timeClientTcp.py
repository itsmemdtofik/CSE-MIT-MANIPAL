import socket

connSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 9991
connSocket.connect((HOST, PORT))
clientTime = connSocket.recv(1024)
print("Current time from server : ", clientTime.decode())
connSocket.close()