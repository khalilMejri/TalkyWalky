import pika


class SenderBroker():
    def __init__(self, user=None):
        self.user = user

    def connect(self, exchange=None):
        self.exchange = exchange
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(
            exchange=exchange, exchange_type='fanout')
        
    def direct_connect(self, exchange=None):
        self.exchange = exchange
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(
            exchange=exchange, exchange_type='direct')


    def send_message(self, msg='echo', key=''):
        self.channel.basic_publish(
            exchange=self.exchange, routing_key=key, body=msg)
        print(" [x] Sent %r" % msg)


    def disconnect(self):
        self.connection.close()
