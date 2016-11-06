#!/usr/bin/env python
#-*-coding:utf-8-*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.92.201'))
channel = connection.channel()

channel.queue_declare(queue='hello2',durable=True)

channel.basic_publish(exchange='',
                      routing_key='hello2',
                      body='Hu YDXXXXX',
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      )
                      )
print("[x] Sent 'Hu Yuedong!'")
connection.close()