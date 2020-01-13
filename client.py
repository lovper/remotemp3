import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
while True:
    svstr = input('Chat> ')
    svbyte = svstr.encode('utf-8')
    s.send(svbyte)
    s.close()


