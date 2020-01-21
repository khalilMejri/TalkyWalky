import pika

class Server:
    def __init__(self):
        self.connected_users = {}
    def connect(self):
        self.connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.receive()
    def receive(self):
        self.channel.queue_declare(queue='main_queue', durable=True)

        def callback(ch, method, properties, body):
            # Received a Message
            
            tokens = body.decode().split('::')
            action = tokens[0]
            tokens[1] =  'amq.'+tokens[1]
            print("received this ",body)
            self.handleAction(action,tokens[1:])
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_consume(queue='main_queue', on_message_callback=callback)
        print('Server Started !! Listening')
        self.channel.start_consuming()
        
    def handleAction(self,action,tokens):
        if action =='login':
            # User send this action + his queue name + his name
            queue_name = tokens[0]
            user_name= tokens[1]
            self.connected_users.setdefault(queue_name,user_name)
            self.send(queue_name,"connected::")

        elif action =='quit':
            # User send his queue name
            queue_name = tokens[0]
            if queue_name in self.connected_users.keys():
                del self.connected_users[queue_name]
                self.send(queue_name,"disconnected::")
                return True
            else:
                self.send(queue_name,"invalid::")
                return False
        elif action =='getConnectedUsers':
            # return all connected Users names
            queue_name = tokens[0]
            usersNames = ','.join(self.connected_users.values())
            self.send(queue_name,"connectedUsers::"+usersNames)
            
        elif action =='getUserData':
            # return a user queue name 
            queue_name = tokens[0]
            demanded_user_name = tokens[1]
            for key,val in self.connected_users.items():
                if val == demanded_user_name:
                    self.send(queue_name,"userQueue::"+str(key))
                    return True
            self.send(queue_name,"notfound::")
            return False

    def send(self,client_queue,msg):
        self.channel.exchange_declare(exchange='users_exchange', exchange_type='direct')
        
        self.channel.basic_publish(
            exchange='users_exchange',
            routing_key=client_queue[4:],
            body=msg,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))

s = Server()
s.connect()