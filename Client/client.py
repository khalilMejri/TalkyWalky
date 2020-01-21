import socket,threading,tkinter
host = socket.gethostname()
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (host,port)


address = (host,port)
s.connect(address)