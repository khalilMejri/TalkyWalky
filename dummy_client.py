import pika



connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def send(channel,message):
    channel.basic_publish(
    exchange='',
    routing_key='main_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
    print('Client send request with queue '+str(queue_name),message)

def callback(ch, method, properties, body):
    print('Received ',body)
    channel.close()
    connection.close()
    

# declaring the server queue
#channel.queue_declare(queue='main_queue', durable=True)

# declaring the exchange and my queue as client
channel.exchange_declare(exchange='users_exchange', exchange_type='direct')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='users_exchange', queue=queue_name,routing_key=queue_name[4:])
send(channel,"login::"+queue_name[4:]+"::"+"Dali")
channel.basic_consume(
            queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()




