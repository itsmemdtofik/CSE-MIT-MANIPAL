import socket
import os

host = socket.gethostname()
port = 9113
conn = socket.socket()
conn.connect((host, port))
conn.send(b'Welcome User !')
msg = conn.recv(1024)
conn.close()
print(repr(msg))