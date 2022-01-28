import socket

s = socket.socket()

print("Socket Create")
s.bind(('localhost', 9999))
s.listen(3)
print("waiting for Connections")
while True :
    c,addr = s.accept()
    name =c.recv(1024).decode()
    print("Connected with",addr,name)
    c.send(bytes('Welcome ','utf-8'))
    c.close()





