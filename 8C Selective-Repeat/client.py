import socket
import random

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
ACKNOWLEDGE=None
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send(msg):
    message=str(msg).encode(FORMAT)
    client.send(message)

def dispMessage(arr):
    for i in arr:
        if (i==-1):
            print("Packet Lost!")
        else:
            print(i)

client.connect(ADDR)
packetCount=int(client.recv(HEADER).decode(FORMAT))
print(f"Packets expected: {packetCount}")
message=[]
missed=[]
isDone=False
index=0
while index<packetCount:
    incoming=client.recv(HEADER).decode(FORMAT)
    if random.randint(0,1):
        message.append(incoming)
        print(incoming)
    else:
        message.append(-1)
        missed.append(index)
    index+=1
print("Packets Received so far:")
dispMessage(message)
if missed:
    for index in missed:
        send(index)
        incoming=client.recv(HEADER).decode(FORMAT)
        message[index]=incoming
send(-1)
print("Another attempt")
dispMessage(message)



