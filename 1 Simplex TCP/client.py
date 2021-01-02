import socket

HEADER=64
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!Disconnect"

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)


while True:
    print('Type exit if you wanna close connection')
    msg=input('Message: ')
    if msg=='exit':
        send(DISCONNECT_MESSAGE)
        break
    else:
        send(msg)