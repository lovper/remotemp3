import socket, _main

with open('config.ini', "r") as f:
    if f.mode == 'r':
        for line in f:
            exec(line)
    else:
        print('Error reading settings')


main = _main.Main(dir)

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
c, addrs = s.accept()
print('CONNECTED: ', addrs)


while True:
    r = c.recv(1024).decode('utf-8')
    returnstr = main.inp(r)
    returnbyte = returnstr.encode('utf-8')
    c.send(returnbyte)
