import socket
import threading

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
file = open('lorem.txt','rb')
file = file.read(1024)

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"{addr} joined")
    conn.send(file)
    print("File Sent")
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
