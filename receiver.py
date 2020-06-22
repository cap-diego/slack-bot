#!/usr/bin/env python
import pika

def callback(ch, method, properties, body):
    """ This is the callback that is going to be executed when a msj is received. Pika call it."""
    print(" [x] Received %r" % body)

if __name__ == '__main__':

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    
    """ the queue must exists """
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


