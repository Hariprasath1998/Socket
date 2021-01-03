import socket
import threading

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!Disconnect"

def toASCII(str):
    res = ' '.join(format(ord(i), 'b') for i in str)
    return res

def handle_client(conn,addr):
    print(f"[New Connection] {addr} connected.")
    connected=True
    while connected:
        data=conn.recv(HEADER).decode(FORMAT)
        if data==DISCONNECT_MESSAGE:
            connected=False
        # print(f"[{addr}] {data}")
        print(f"Input from[{addr}]: {data}")
        print(f"ASCII value of {data}")
        print(toASCII(data))
    conn.close()
    print(f"connection closed for {addr}")


def start():
    print("[STARTING]......")
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"Server Listening on {SERVER}:{PORT}")
    while True:
        conn, addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"Active Connections: {threading.active_count()-1}")


start()
