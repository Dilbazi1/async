
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
LOGGER=logging.getLogger('client')
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(clientlog_file)
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
