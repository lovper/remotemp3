import socket
import _main

with open('config.ini', "r") as f:
    if f.mode == 'r':
        for line in f:
            exec(line)
    else:
        print('Error reading settings')


def pslisten():
    global c
    s.listen(5)
    c, addrs = s.accept()
    print('CONNECTED: ', addrs)


main = _main.Main(dir)

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

pslisten()

while True:
    try:
        r = c.recv(1024).decode('utf-8')
    except:
        pslisten()
        continue
    returnstr = main.inp(r)
    returnbyte = returnstr.encode('utf-8')
    try:
        c.send(returnbyte)
    except:
        pslisten()
        continue

