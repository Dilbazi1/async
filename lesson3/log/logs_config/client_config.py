
import sys
import os
import logging

sys.path.append('../')
client_formatter= logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')
# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, '../logs_files/client.log')

STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(client_formatter)
STREAM_HANDLER.setLevel(logging.ERROR)

clientlog_file= logging.FileHandler(PATH, encoding='utf8')
clientlog_file.setFormatter(client_formatter)
client_log=logging.getLogger('client')
client_log.setLevel(logging.DEBUG)
client_log.addHandler(STREAM_HANDLER)
client_log.addHandler(clientlog_file)
if __name__ == '__main__':
    client_log.critical('Критическая ошибка')
    client_log.critical('Критическая ошибка')
    client_log.error('Ошибка')
    client_log.debug('Отладочная информация')
    client_log.info('Информационное сообщение')
