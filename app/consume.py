import os

from provenance.capture import Logger
from provenance.amqp import Subscriber
from couch import CouchLogger

couch_logger = CouchLogger.from_environment()
stdout_logger = Logger.stdout()

logger = Logger.fanout([couch_logger, stdout_logger])

amqp_host = os.environ.get('AMQP_HOST', 'localhost')
amqp_exchange = os.environ.get('AMQP_EXCHANGE', 'provenance')

subscriber = Subscriber(amqp_host, amqp_exchange, logger)

subscriber.start()
