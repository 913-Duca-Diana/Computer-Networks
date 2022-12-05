import json
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",5557))
l=[1,2,3,4,5]
data=json.dumps({'values':l})
s.send(data.encode())
print("sum is: "+s.recv(1024).decode())
s.close()