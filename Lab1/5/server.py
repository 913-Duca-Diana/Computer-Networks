import json
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",5559))
s.listen(5)
print("Waiting for client...\n")

cs,a=s.accept()
data=cs.recv(1024)
data=json.loads(data.decode())

s='['
k=int(data.get("value"))
for i in range(1,k):
    if k%i==0:
        s=s+" "+str(i)+','
s=s+"]"
cs.send(str(s).encode())
cs.close()