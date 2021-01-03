import socket
import random

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
ACKNOWLEDGE=None
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send(lastIndex):
    message=str(lastIndex).encode(FORMAT)
    client.send(message)

def dispMessage(arr):
    for i in arr:
        print(i)

client.connect(ADDR)
packetCount=int(client.recv(HEADER).decode(FORMAT))
print(f"Packets expected: {packetCount}")
message=[]
lastIndex=(random.randint(0,packetCount))
print(lastIndex)
index=0
while index<packetCount:
    incoming=client.recv(HEADER).decode(FORMAT)
    if index<=lastIndex:
        message.append(incoming)
        print(incoming)
    index+=1
print("Packets Received so far:")
dispMessage(message)
if(lastIndex==packetCount):
    print("Packets received at first try")
else:
    print("Missing some packets: Retrying.....")

send(lastIndex)
index=0
if(lastIndex!=packetCount):
    while index<(packetCount-(lastIndex+1)):
        incoming=client.recv(HEADER).decode(FORMAT)
        if index<lastIndex:
            message.append(incoming)
        index+=1
    print("Final Attempt...")
    dispMessage(message)


