#!/usr/bin/env python
#-*-coding:utf-8-*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.92.201'))

channel = connection.channel()

channel.queue_declare(queue='hello2',durable=True)

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    # ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello2',
                      # no_ack=True
)
print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()