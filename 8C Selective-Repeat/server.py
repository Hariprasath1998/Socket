import socket

HEADER=1024
PORT=8900
SERVER= 'localhost'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handle_client(conn,addr):
    print(f"[New Connection] {addr} connected.")
    size=input('Number of packets to send: ')
    conn.send(size.encode(FORMAT))
    message=[]
    isDone=False
    for i in range(0,int(size)):
        message.append(input(f'Packet #{i+1}: '))
    for i in message:
        print(i)
    index=0
    while index<int(size):
        print(f"Sending packet#{index+1}")
        conn.send(message[index].encode(FORMAT))
        print(f"Packet#{index+1} sent")
        index+=1
    while not isDone:
        ack=int(conn.recv(HEADER))
        if(ack==-1):
            isDone=True
        else:
            index=ack
            conn.send(message[index].encode(FORMAT))
    conn.close()
    print("Connection closed")

def start():
    print("[STARTING]......")
    server.bind(ADDR)
    server.listen()
    print(f"Server Listening on {SERVER}:{PORT}")
    while True:
        conn, addr=server.accept()
        handle_client(conn,addr)

start()
