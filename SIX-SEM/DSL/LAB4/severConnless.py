import socket
import os

connSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpHost = socket.gethostname()
udpPort = 1234
connSocket.bind((udpHost, udpPort))
while True:
    print("Waiting for client...")
    data, clientAddr = connSocket.recvfrom(1024)
    print("Received Messages : ", data.decode(), "from", clientAddr)
