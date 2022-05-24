import socket
HOST = '172.16.57.223'
PORT = 31620
s = socket.socket()
s.bind((HOST, PORT))
s.listen()
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
name = input(str("Enter your name: "))
conn.send(name.encode())
while True:
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me: "))
    if message == "[e]":
     message = "Left chat room!"
     conn.send(message.encode())
     print("\n")
     break
    conn.send(message.encode())
