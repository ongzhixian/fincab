import json
import logging

class StructuredLogMessage(object):
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        if self.kwargs == {}:
            return '%s' % (self.message)
        else:
            return '%s | %s' % (self.message, json.dumps(self.kwargs))

sm = StructuredLogMessage   # optional, to improve readability

class Logger(object):
    """
    Singleton logger
    Log Levels
    ----------
    CRITICAL    50
    ERROR       40
    WARNING     30
    INFO        20
    DEBUG       10
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            cls.initialize_log_configuration()
        return cls._instance

    def initialize_log_configuration():
        logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s.%(msecs)06d %(name)-12s %(levelname)-8s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
            )
        logging.getLogger('pika').setLevel(logging.WARNING)
        print("reset")

    def debug(self, message, **kwargs):
        """DEBUG : 10"""
        logging.debug(sm(message, **kwargs))

    def info(self, message, **kwargs):
        """INFO : 20"""
        logging.info(sm(message, **kwargs))

    def warn(self, message, **kwargs):
        """WARNING : 30"""
        logging.warn(sm(message, **kwargs))

    def error(self, message, **kwargs):
        """ERROR : 40"""
        logging.error(sm(message, **kwargs))

    def critical(self, message, **kwargs):
        """CRITICAL : 50"""
        logging.critical(sm(message, **kwargs))

# Exports



log = Logger()
