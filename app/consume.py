import os

from provenance.capture import Logger, Subscriber
from couch import CouchLogger

couch_logger = CouchLogger.from_environment()
stdout_logger = Logger.stdout()

logger = Logger.fanout([couch_logger, stdout_logger])

amqp_host = os.environ.get('RABBITMQ_HOST', 'localhost')
amqp_user = os.environ.get('RABBITMQ_USER', 'guest')
amqp_password = os.environ.get('RABBITMQ_PASSWORD', 'guest')
amqp_exchange = os.environ.get('RABBITMQ_EXCHANGE', 'provenance')

subscriber = Subscriber(logger, amqp_host, amqp_user, amqp_password, amqp_exchange)

subscriber.start()
