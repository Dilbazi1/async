import subprocess
import shlex
import time
import os
import signal


PROCESS = []

while True:

    ANSWER = input('Выберите действие: q - выход, s - запустить сервер и клиенты, x - закрыть все окна: ')

    if ANSWER == 'q':
        break
    elif ANSWER == 's':
        PROCESS.append(subprocess.Popen('gnome-terminal -- python3 server.py', shell=True))
        time.sleep(0.5)
    elif ANSWER=='k':
        print('Убедитесь, что на сервере зарегистрировано необходимо количество клиентов с паролем 123456.')
        print('Первый запуск может быть достаточно долгим из-за генерации ключей!')
        clients_count = int(
            input('Введите количество тестовых клиентов для запуска: '))
        # Запускаем клиентов:
        for i in range(clients_count):
            PROCESS.append(subprocess.Popen(f'gnome-terminal -- python3 client.py -n test{i+1} -p 123456', shell=True))

    elif ANSWER == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()
            VICTIM.terminate()