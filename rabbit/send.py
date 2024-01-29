import pika
try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='first')

    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='HELLLOOO')
    print(" [x] Sent 'Hello World!'")
    connection.close()
except KeyboardInterrupt:
    print('Goodbye!')