import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

client = True
while client:
    svstr = input('Input> ')
    svbyte = svstr.encode('utf-8')
    s.send(svbyte)
    if svstr == 'stop':
        client = False
s.close()

