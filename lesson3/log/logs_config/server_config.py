
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

server_log=logging.getLogger('server')
server_log.setLevel(logging.DEBUG)
server_log.addHandler(stream_handler)
server_log.addHandler(serverlog_file)
if __name__ == '__main__':
    server_log.critical('Критическая ошибка')
    server_log.critical('Критическая ошибка')
    server_log.error('Ошибка')
    server_log.debug('Отладочная информация')
    server_log.info('Информационное сообщение')