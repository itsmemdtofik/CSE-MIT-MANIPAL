import socket

HOST = 'localhost'
PORT = 1999
connSocket = socket.socket()
connSocket.bind((HOST, PORT))
connSocket.listen()
print("Waiting for incoming connection...\n")
clientConn, clientAddr = connSocket.accept()
print("Received connection from : ", clientAddr[0], "(", clientAddr[1], ")\n")
s_name = clientConn.recv(1024)
s_name = s_name.decode()
print(s_name, "Has connected to the chat room\nEnter [e] to exit chat room\n")
name = input(str("Enter your name : "))
clientConn.send(name.encode())
while True:
    msg = input(str("Me : "))
    if msg == "[e]":
        msg = "Left Chat room"
        clientConn.send(msg.encode())
        print("\n")
        break
    clientConn.send(msg.encode())
    msg = clientConn.recv(1024)
    msg = msg.decode()
    print(s_name, ":", msg)
