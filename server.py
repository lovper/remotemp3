import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
c, addrs = s.accept()
print('CONNECTED: ', addrs)
while True:
    r = c.recv(1024)
    r = r.decode('utf-8')
    if r != 'stop':
        print(r)
    else:
        break
