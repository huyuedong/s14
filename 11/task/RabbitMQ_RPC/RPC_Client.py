#!/usr/bin/env python
#-*-coding:utf-8-*-

import pika
import subprocess
import os
import sys

def excute(cmd):
    result = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    return result.stdout.read()

def on_request(ch, method, props, body):
    body = str(body)
    result = excute(body)
    h = subprocess.Popen("hostname",shell=True,stdout=subprocess.PIPE)
    hostname = h.stdout.read()
    response = """
    Hostname:%s
    execute result:
    %s
    """ % (hostname,str(result))
    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)

def run():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672))

    channel = connection.channel()
    channel.queue_declare(queue="rpc_queue", durable=False)
    channel.exchange_declare(exchange="cmd",exchange_type="fanout",)
    channel.queue_bind(exchange="cmd",queue="rpc_queue")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request,queue="rpc_queue")
    channel.start_consuming()

if __name__ == '__main__':
    run()