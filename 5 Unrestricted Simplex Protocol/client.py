import socket

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!Disconnect"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    client.send(message)


while True:
    print('Type exit if you wanna close connection')
    msg=input('Message: ')
    if msg=='exit':
        send(DISCONNECT_MESSAGE)
        break
    else:
        send(msg)