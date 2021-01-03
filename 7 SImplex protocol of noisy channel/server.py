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
    for i in range(0,int(size)):
        message.append(input(f'Packet #{i+1}: '))

    for i in range(0,int(size)):
        while True:
            print(f"Sending packet#{i+1}")
            conn.send(message[i].encode(FORMAT))
            ack=int(conn.recv(HEADER).decode(FORMAT))
            print(ack)
            if ack==1:
                print(f"Acknowledgement received for packet#{i+1}")
                break
            else:
                print("No Acknowledgement")
                print("Retrying.....")

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
