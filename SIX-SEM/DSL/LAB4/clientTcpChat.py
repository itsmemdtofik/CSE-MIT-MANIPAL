import socket

HOST = 'localhost'
PORT = 1999
connSocket = socket.socket()
name = input("Enter your name : ")
print("\n Trying to connect to ", HOST, "(", PORT, ")\n")
connSocket.connect((HOST, PORT))
print("Connected...\n")
connSocket.send(name.encode())
s_name = connSocket.recv(1024)
s_name = s_name.decode()
print(s_name, "Has joined to the chat room\nEnter [e] to exit chat room\n")
while True:
    msg = connSocket.recv(1024)
    msg = msg.decode()
    print(s_name, ":", msg)
    msg = input(str('Me : '))
    if msg == "[e]":
        msg = "Left the room"
        connSocket.send(msg.encode())
        print("\n")
    connSocket.send(msg.encode())