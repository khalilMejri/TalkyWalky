import pika
from threading import Thread


class ReceiverBroker():
    def __init__(self, user=None, handler=None):
        self.user = user
        self.handler = handler

    def connect(self, exchange=None):
        self.exchange = exchange
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()
        self.channel.exchange_declare(
            exchange=exchange, exchange_type='fanout')
        result = self.channel.queue_declare(queue='', exclusive=True)

        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=exchange, queue=self.queue_name)
        print(' [*] Waiting for msgs. To exit press CTRL+C')

    def listen_channel(self, cb):
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=cb, auto_ack=True)
        self.channel.start_consuming()
        print("shutdown broker!")

    def async_consumer(self, cb):
        worker = Thread(target=self.listen_channel, args=[cb])
        worker.start()

    def discard_channel(self):
        self.channel.stop_consuming()
        # self.connection.close()
