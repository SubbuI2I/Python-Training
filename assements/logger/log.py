import logging
from logging.handlers import TimedRotatingFileHandler


class Log:
    def __init__(self):
        return None

    def write_log(self, msg, loglevel=logging.DEBUG):
        # logging.basicConfig(filename='./logger/log_files/logs.log', # temporary for learning using basic config
        #                     format="%(asctime)s - %(levelname)s - [%(name)s:%(lineno)s] - %(message)s")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - [%(name)s:%(lineno)s] - %(message)s")
        logger = logging.getLogger('timed_logger')
        timed_handler = TimedRotatingFileHandler(
            'logger/log_files/timed.log', when='m', interval=1, backupCount=2)
        timed_handler.setFormatter(formatter)
        timed_handler.setLevel(logging.DEBUG)
        logger.addHandler(timed_handler)

        if (msg):
            logger.log(loglevel, msg)
        else:
            logger.log(loglevel, 'No errors to log ')



def get_logger(name): # just for testing different approace and learning.

    # logging.basicConfig(filename='./logger/log_files/logs.log',
    #                     format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(name)
    return logger
