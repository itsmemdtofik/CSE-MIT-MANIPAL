import socket
import os

HOST = 'localhost'
PORT = 2020
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((HOST, PORT))
    conn.sendall(b'Hello World')
    data = conn.recv(1024)
    print('Receieved Connection')
    print('Server :', data.decode())