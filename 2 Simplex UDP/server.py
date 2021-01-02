import socket
import threading


PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'

server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[New Connection] {addr} connected.")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            print(f"[{addr}] {msg}")
    print('connection closed')
    conn.close()


def start():
    while True:
        data, addr=server.recvfrom(4096)
        print(f"Client: {data.decode(FORMAT)}")
        message=bytes(("Connected!").encode(FORMAT))
        server.sendto(message,addr)
        
print("[STARTING]......")
start()
