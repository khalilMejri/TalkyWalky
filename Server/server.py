import socket, threading
host = socket.gethostname()
port = 4000

clients = {}
addresses = {}
print(host)
print("Server is ready...")
serverRunning = True
'''
def handle_client(conn):
    try:
        data = conn.recv(1024).decode('utf8')
        welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % data
        conn.send(bytes(welcome, "utf8"))
        msg = "%s has joined the chat" % data
        broadcast(bytes(msg, "utf8"))
        clients[conn] = data
        while True:
            found = False
            response = 'Number of People Online\n'
            msg1 = conn.recv(1024) 

            if msg1 != bytes("{quit}", "utf8"):
                broadcast(msg1, data+": ")
            else:
                conn.send(bytes("{quit}", "utf8"))
                conn.close()
                del clients[conn]
                broadcast(bytes("%s has left the chat." % data, "utf8"))
                break
    except:
        print("%s has left the chat." % data)
def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)
'''

while True:
    conn,addr = s.accept()
    conn.send("Enter username: ".encode("utf8"))
    print("%s:%s has connected." % addr)
    addresses[conn] = addr
    print(conn,addr)
    #hreading.Thread(target = handle_client, args = (conn,)).start()


class ClientHandler(threading.Thread):
    def __init__(self,conn,addr):
        self.conn = conn
        self.addr = conn
        pass
    
    def client_demande_data(self):
        pass
    def client_choose_room(self,client,room):
        pass
    def client_choose_client(self,client1,client2):
        pass
    def client_send_msg_to_room(self,client,room,message):
        pass
    # the main program for the handler
    def run():
        pass
    def quit():
        pass
    

class Server(threading.Thread):
    def __init__(self,host,port):
        self.host = host
        self.port = port 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen()
    def run():
        while True:
            with self.lock:
                try:
                    connection, address = self.sock.accept()
                except socket.error:
                    time.sleep(0.05)
                    continue

            connection.setblocking(False)
            if connection not in self.connection_list:
                self.connection_list.append(connection)

            self.message_queues[connection] = queue.Queue()
            