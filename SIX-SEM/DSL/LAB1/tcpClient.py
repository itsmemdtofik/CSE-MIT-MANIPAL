from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, World')
data = s.recv(1024)
print(data)
s.close()
