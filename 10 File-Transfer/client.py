import socket

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
file = open('Received_file.txt','wb')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print("Connected to server")

Receive = client.recv(1024)
file.write(Receive)
print("File Received")

file.close()
print ("Successfully Received the file")

client.close()        



