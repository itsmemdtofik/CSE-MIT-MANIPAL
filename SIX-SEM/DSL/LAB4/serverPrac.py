import socket
import os
host = socket.gethostname()
port = 9113
conn = socket.socket()
conn.bind((host, port))
conn.listen(5)
(connClient, clientAddr) = conn.accept()
print('Get connection from', clientAddr[0], '(', clientAddr[1], ')')
print("Thank you for connecting \n")
while True:
    msg = connClient.recv(1024)
    if not msg:
        break
connClient.close()
