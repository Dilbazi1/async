import inspect
import logging
import sys
import traceback



from client import create_arg_parser

if sys.argv[0].find('client')==-1:
     LOGGER = logging.getLogger('server')
else:
     LOGGER=logging.getLogger('client')
def log(func):
   def log_call(*args,**kwargs)  :
     res=func(*args,**kwargs)
     LOGGER.debug(
           f'Функция {func.__name__} параметр {args},{kwargs}'
                f'модуль {func.__module__}'
                f'вызов из функции {traceback.format_stack()[0].strip().split()[-1]}'
                f'вызов из функции{inspect.stack()[1][3]}',stacklevel=2)


     return res
   return log_call

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
