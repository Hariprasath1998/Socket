import socket


PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
HEADER=1024
connection=True

def send(msg):
    client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Connected to server!")
    client.sendto(msg.encode(FORMAT),ADDR)
    print("Message sent")
    client.close()
    print("Connection closed!")

while connection:
    # send(input('Message to Server: '))
    print('Type exit if you wanna close connection')
    msg=input('Message to Server: ')
    if msg=='exit':
        break
    else:
        send(msg)
