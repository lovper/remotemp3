import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

client = True
while client:
    svstr = input('Input> ')
    if not svstr:
        continue
    svbyte = svstr.encode('utf-8')
    s.send(svbyte)
    r = s.recv(1024).decode('utf-8')
    if r == 'exit':
        break
    else:
        print(r)
s.close()

