import socket
import threading
from random import randrange


PORT= 5050
SERVER=socket.gethostbyname(socket.gethostname()) #ipaddress of local conn
ADDR=(SERVER,PORT)
FORMAT='utf-8'


n=str(randrange(100000))
print("The generated number is: "+ n)
nrDigits=len(n)

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} CONNECTED.\n")
    # sending message to the client
    conn.send(str(nrDigits).encode(FORMAT))


    connected = True
    while connected:
        #recieving message from the client
        msg_lenght = conn.recv(1024).decode(FORMAT)
        if msg_lenght:
            msg_lenght=int(msg_lenght)
            msg=conn.recv(msg_lenght).decode(FORMAT)
            #print(f"[{addr}] {msg}")
            if(int(msg)>int(n)):
                #sending message to the client
                conn.send("The number is too big".encode(FORMAT))
            elif (int(msg) < int(n)):
                # sending message to the client
                conn.send("The number is too small".encode(FORMAT))
            else:
                print(f"The client [{addr}] guessed the number")
                conn.send("You guessed the number".encode(FORMAT))
                connected=False


    conn.close()

def start():
    s.listen()
    print(f"[LISTENING]  Server is listening on {SERVER}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
print("[STARTING] server is starting...")
start()
