
import logging.handlers
import logging
import os
import sys
sys.path.append('../')
server_formatter=logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, '../logs_files/server.log')

stream_handler=logging.StreamHandler(sys.stderr)
stream_handler.setFormatter(server_formatter)
stream_handler.setLevel(logging.ERROR)

serverlog_file=logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='S')
serverlog_file.setFormatter(server_formatter)

LOGGER=logging.getLogger('server')
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(stream_handler)
LOGGER.addHandler(serverlog_file)
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')