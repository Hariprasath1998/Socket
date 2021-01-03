import socket
import random

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
ACKNOWLEDGE=None
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def send(ack):
    message=ack.encode(FORMAT)
    client.send(message)

def msgDisplay():
    if (random.randint(0,1))==1:
        print(client.recv(HEADER).decode(FORMAT))
        send('1')
    else:
        print('Packet Lost')
        send('0')

def start():
    client.connect(ADDR)
    packetCount=int(client.recv(HEADER).decode(FORMAT))
    print(packetCount)
    for i in range(packetCount):
        print(f'Packet#{i+1}')
        msgDisplay()
        
        
        
start()

