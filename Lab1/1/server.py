import json
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",5557))
s.listen(5)

cs,a=s.accept()
data=cs.recv(1024)
data=json.loads(data.decode())

s=0
for e in data.get("values"):
    s+=e
cs.send(str(s).encode())
cs.close()