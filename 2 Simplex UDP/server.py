import socket

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def start():
    print(f"Server @ : {ADDR}")
    while True:
        data, addr=server.recvfrom(4096)
        print(f"Client {addr}: {data.decode(FORMAT)}")
        
start()
