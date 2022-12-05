import json
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",5553))
l='sefiw eerht sah letsoC'
data=json.dumps({'value':l})
s.send(data.encode())
print("The reversed string is:  "+s.recv(1024).decode())
s.close()