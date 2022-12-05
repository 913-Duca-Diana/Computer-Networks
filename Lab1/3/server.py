import json
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",5553))
s.listen(5)
print("Waiting for client...\n")

cs,a=s.accept()
data=cs.recv(1024)
data=json.loads(data.decode())

s=''
for e in data.get("value"):
    s=e+s
cs.send(str(s).encode())
cs.close()