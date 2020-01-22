import socket,threading,tkinter
host = socket.gethostname()
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (host,port)


address = (host,port)
s.connect(address)

class Client(threading.Thread):
    def __init__(self):
        pass
    
    def connect_to_server(self)
    
    def send_data_request(self):
        pass
    def select_room(self,server,room):
        pass
    def select_client(self,server,client):
        pass
    def get_dest_pubKey(self, dest):
        pass
    def send_msg(self, dest, message):
        pass
    def receive_msg(self, message):
        pass
    # the main program for the client
    def run():
        pass
    def quit():
        pass
    