#!/usr/bin/env python
#-*-coding:utf-8-*-
import pika
import uuid

class rpc_master_cmd(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',port=5672))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_queue',durable=True)
        result = self.channel.queue_declare(exclusive=True)
        self.channel.exchange_declare(exchange="cmd",exchange_type="fanout")
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,no_ack=True,queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self,cmd):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='cmd',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                       ),
                                   body=str(cmd)
                                   )
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)

def run():
    cmd = input(">>>:").strip()
    cmd_rpc = rpc_master_cmd()
    response = str(cmd_rpc.call(cmd).decode())
    print(response)

if __name__ == '__main__':
    run()