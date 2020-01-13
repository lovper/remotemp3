import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
    c, addrs = s.accept()
    print('CONNECTED: ', addrss)
    r=c.recv(1024)
    print(r.decode('utf-8'))
    c.close()