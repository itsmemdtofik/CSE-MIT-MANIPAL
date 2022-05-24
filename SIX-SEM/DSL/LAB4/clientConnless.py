import socket
import os

connSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpHost = socket.gethostname()
udpPort = 12345
msg = "UDP Program"
print("UDP target IP : ", udpHost)
print("UDP target PORT", udpPort)
connSocket.sendto(msg.encode(), (udpHost, udpPort))