import inspect
import json
import socket
import sys
import argparse
import logging
import traceback


import log.logs_config.server_config
from errors import IncorrectDataRecivedError
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, PRESENCE, \
    TIME, USER, ERROR, DEFAULT_PORT
from common.utils import get_message, send_message
from decorator import Log
from decorator import log

LOGGER = logging.getLogger('server')











# @Log()
@log
def process_client_message(message):
    """
       Обработчик сообщений от клиентов, принимает словарь - сообщение от клинта,
       проверяет корректность, возвращает словарь-ответ для клиента
       :param message:
       :return:
       """
    LOGGER.debug(f'Разбор сообщения от клиента : {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message and \
            USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'

    }

# @Log()
@log
def create_arg_parser():
    """
    Парсер аргументов коммандной строки
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    return parser


def main():
    """
        Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию
        :return:
        """
    parser = create_arg_parser()
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    # проверка получения корретного номера порта для работы сервера.
    if not 1023 < listen_port < 65536:
        LOGGER.critical(f'Попытка запуска сервера с указанием неподходящего порта '
                            f'{listen_port}. Допустимы адреса с 1024 до 65535.')
        sys.exit(1)
    LOGGER.info(f'Запущен сервер, порт для подключений: {listen_port}, '
                    f'адрес с которого принимаются подключения: {listen_address}. '
                    f'Если адрес не указан, принимаются соединения с любых адресов.')
    # Готовим сокет

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт

    transport.listen(MAX_CONNECTIONS)



    while True:
        client, client_address = transport.accept()
        LOGGER.info(f'Установлено соедение с ПК {client_address}')
        try:
            message_from_cient = get_message(client)
            LOGGER.debug(f'Получено сообщение {message_from_cient}')
            response = process_client_message(message_from_cient)
            LOGGER.info(f'Cформирован ответ клиенту {response}')
            send_message(client, response)
            LOGGER.debug(f'Соединение с клиентом {client_address} закрывается.')
            client.close()
        except json.JSONDecodeError:
            LOGGER.error(f'Не удалось декодировать JSON строку, полученную от '
                             f'клиента {client_address}. Соединение закрывается.')
            client.close()
        except IncorrectDataRecivedError:
            LOGGER.error(f'От клиента {client_address} приняты некорректные данные. '
                             f'Соединение закрывается.')
            client.close()


if __name__ == '__main__':
    main(

    )
