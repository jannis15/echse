import logging
from logging.handlers import RotatingFileHandler


class MyLogger:
    def __init__(self, name, filename, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        handler = RotatingFileHandler(filename=filename, mode='a', maxBytes=1024, backupCount=3)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)


log = MyLogger(name='my_logger', filename='echse.log').logger
