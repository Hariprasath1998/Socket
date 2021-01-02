import socket


PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
connection=True
message="I am Client"


def send(msg):
    client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(msg.encode(FORMAT),ADDR)
    data,addr=client.recvfrom(4096)
    print(f"Server: {data.decode(FORMAT)}")
    client.close()

while connection:
    send(input('Message to Server: '))

# send('wassup')