import logging
from logging.handlers import TimedRotatingFileHandler


class Log:
    def __init__(self):
        return None

    def write_log(self, msg, loglevel=10):
        logging.basicConfig(filename='./logger/log_files/logs.log',
                            format="%(asctime)s - %(levelname)s - [%(name)s:%(lineno)s] - %(message)s")
        if (msg):
            logging.info(msg)
        else:
            logging.log(loglevel, 'No errors to log ')


def get_logger(name):
    # logging.basicConfig(filename='./logger/log_files/logs.log',
    #                     format="%(asctime)s - %(levelname)s - %(message)s")
    logger = logging.getLogger(name)
    return logger
