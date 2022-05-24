import socket
import time

connSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = socket.gethostname()
PORT = 9991
connSocket.bind((HOST, PORT))
connSocket.listen(5)
while True:
    connClient, clientAddr = connSocket.accept()
    print("Got a connection from %s" % str(clientAddr))
    currentTime = time.ctime(time.time()) + "\r\n"
    connClient.send(currentTime.encode('ascii'))
    connClient.close()