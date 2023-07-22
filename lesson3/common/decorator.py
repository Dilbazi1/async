import inspect
import logging
import sys
import traceback
import log.logs_config.client_config
import log.logs_config.server_config



if sys.argv[0].find('client')==-1:
     LOGGER = logging.getLogger('server')
else:
     LOGGER=logging.getLogger('client')

def log(func_to_log):
    """Функция-декоратор"""
    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} c параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__}')
        return ret
    return log_saver

class Log:
    def __call__(self, func):
        def log_call(*args,**kwargs):
            res = func(*args, **kwargs)
            LOGGER.debug(
                f'Функция {func.__name__} параметр {args},{kwargs}'
                f'модуль {func.__module__}'
                f'вызов из функции {traceback.format_stack()[0].strip().split()[-1]}'
                f'вызов из функции{inspect.stack()[1][3]}',stacklevel=2)

            return res

        return log_call
