import socket
import threading

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!Disconnect"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"{addr} joined")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
            else:
                print(f"[{addr}] says: {msg}")
    conn.close()
    print(f"{addr} has disconnected.....")


def start():
    server.listen()
    print(f"Server Listening on {SERVER}:{PORT}")
    while True:
        conn, addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"Active Connections: {threading.active_count()-1}")

start()
