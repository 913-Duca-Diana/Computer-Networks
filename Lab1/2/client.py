import json
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",5552))
l='Costel has three wifes'
data=json.dumps({'value':l})
s.send(data.encode())
print("The number of white spaces is "+s.recv(1024).decode())
s.close()