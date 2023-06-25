#tests socket
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(('data.pr4e.ord', 80))
except:
    print("service not known")
cmd = 'GET http://data.pr4e.htm HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()