import socket
import tkinter

top = tkinter.Tk()

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))


arr = []
i = 0

s.send(b'slist')
r = s.recv(1024).decode('utf-8')
for line in r.splitlines():
    arr.append(line)

for obj in arr:
    n = i
    def n():
        s.send(str(i).encode('utf-8'))
    f = tkinter.Button(top, text=obj, command=n)
    f.pack()
    int(i)
    i += 1

# client = True
# while client:
#     svstr = input('Input> ')
#     if not svstr:
#         continue
#     svbyte = svstr.encode('utf-8')
#     try:
#         s.send(svbyte)
#     except:
#         print('Connection lost, exiting...')
#         break
#     r = s.recv(1024).decode('utf-8')
#     if r == 'exit':
#         break
#     else:
#         print(r)


top.mainloop()


s.close()

