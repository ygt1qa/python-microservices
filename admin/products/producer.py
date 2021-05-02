
import pika
import json

params = pika.URLParameters(
    'amqps://ywczldrs:8kTVKyyE_ouOHLmoe1jTjnjNupp-QCtZ@cougar.rmq.cloudamqp.com/ywczldrs')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body),
                          properties=properties)
