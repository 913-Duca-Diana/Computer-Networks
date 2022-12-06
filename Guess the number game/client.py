import socket
from random import randrange
import time

PORT= 5050
SERVER="192.168.56.1"
ADDR=(SERVER,PORT)
FORMAT='utf-8'

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
def recieve():
    # recieving message from the server
    return client.recv(1024).decode(FORMAT)

def send(msg):
    message=msg.encode()
    msg_lenght=len(message)
    #sending message to the server
    send_lenght=str(msg_lenght).encode(FORMAT)
    send_lenght +=b' ' * (1024 -len(send_lenght))
    client.send(send_lenght)
    client.send(message)


nrDigits=int(recieve())
notguessed=True
start=10**(nrDigits-1)
end=10**nrDigits
while notguessed:
    time.sleep(0.30)
    number=randrange(start,end)
    print(number)
    send(str(number))
    s=recieve()
    if s=='The number is too small':
        start=number
        print(s)
    elif s=='The number is too big':
        end=number
        print(s)
    else:
        print(s + " " +str(number))
        notguessed=False



