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

def msgDisplay(ack):
    if ack==1:
        print(client.recv(HEADER).decode(FORMAT))
    else:
        client.recv(HEADER).decode(FORMAT)
        print('Packet Lost')
        print('Retrying....')
    send(str(ack))



def start():
    client.connect(ADDR)
    packetCount=int(client.recv(HEADER).decode(FORMAT))
    print(f"Packets expected: {packetCount}")
    for i in range(packetCount):
        print("")
        while True:
            print(f'Packet#{i+1}')
            ack=(random.randint(0,1))
            msgDisplay(ack)
            if(ack==1):
                break
        
        
        
start()

