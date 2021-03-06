import sys, socket

args = sys.argv
if len(args) > 2:
    ip = args[1]
    port = int(args[2])
    password = args[3]

with socket.socket() as s:
    s.connect((ip, port))
    password = password.encode()
    s.send(password)
    data = s.recv(1024)
    
data = data.decode()
print(data)
