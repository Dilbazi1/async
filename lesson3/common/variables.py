""" Константы"""
import logging

# порт по умолчанию сетевого действия
DEFAULT_PORT=7777
# ип адрес по умолчанию для подключения клиента
DEFAULT_IP_ADDRESS='localhost'
# максимальная длина сообщения в байтах
MAX_PACKAGE_LENGTH=1024
MAX_CONNECTIONS=5
# кодировка проекта
ENCODING='utf-8'
# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG



# протокол  JIM  основные ключи
ACTION='action'
TIME='time'
USER='user'
ACCOUNT_NAME='account_name'


# прочие ключи , используемые в протоколе
PRESENCE='presence'
RESPONSE='response'
ERROR='error'
