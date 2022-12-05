import json
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",5559))
l=1624
data=json.dumps({'value':l})
s.send(data.encode())
print("The divisors are:  "+s.recv(1024).decode())
s.close()