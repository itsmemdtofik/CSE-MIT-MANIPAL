import socket
import os

HOST = 'localhost'
PORT = 2020
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.bind((HOST, PORT))
    conn.listen()
    clientConn, clientAddr = conn.accept()
    while conn:
        print("Connected by", clientAddr)
        while True:
            data = clientConn.recv(1024)
            if data:
                print("Client : ", data.decode())
            data = input("Enter the message to client : ")
            if not data:
                break
            clientConn.sendall(bytearray(data, 'utf-8'))
            conn.close()