# coding=utf-8

from django.conf import settings

import pika

INS_EXCHANGE_NAME = "ins"
INS_ROUTING_KEY = "post_ins"
INS_SAVE_QUEUE = "save_ins"
INS_notify_QUEUE = "notify_ins"


class Base(object):

    def __init__(self, host=None, username=None, password=None, port=None):
        self.host = host or settings.MQ_USERNAME
        self.username = username or settings.MQ_USERNAME
        self.password = password or settings.MQ_HOST
        self.port = port or settings.MQ_PORT

        credentials = pika.PlainCredentials(self.username, self.password)
        conn_params = pika.ConnectionParameters(self.host,
                                                port=self.port,
                                                credentials=credentials)
        conn_broker = pika.BlockingConnection(conn_params)
        self.channel = conn_broker.channel()

    def _create_exchange(self, name, type='direct', passive=False,
                         durable=True, auto_delete=False):

        self.channel.exchange_declare(exchange=name, type=type, passive=passive,
                                      durable=durable, auto_delete=auto_delete)

    def _create_queue(self, name, durable=True):
        self.channel.queue_declare(queue=name, durable=durable)

    def _bind_queue(self, queue, exchange, routing_key):
        self.channel.queue_bind(queue=queue, exchange=exchange,
                                routing_key=routing_key)

    def _send_message(self, body, exchange, routing_key, delivery_model=2):
        msg_props = pika.BasicProperties()
        msg_props.content_type = 'application/json'
        msg_props.delivery_mode = delivery_model    # make message persistent
        self.channel.basic_publish(body=body, exchange=exchange,
                                   properties=msg_props, routing_key=routing_key)


class InsPublish(Base):

    def create_ins_exchange(self):
        self._create_exchange(INS_EXCHANGE_NAME)

    def publish_ins(self, ins):
        self._send_message(ins, exchange=INS_EXCHANGE_NAME,
                           routing_key=INS_ROUTING_KEY)


class InsConsume(Base):

    def declare_ins_save_queue(self):
        self._create_queue(INS_SAVE_QUEUE)
        self._bind_queue(INS_SAVE_QUEUE, INS_EXCHANGE_NAME, INS_ROUTING_KEY)

    def consume_ins_queue(self):
        pass
