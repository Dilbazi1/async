"""Данный вариант будет рабоать только у меня(ну может еще у кого запустится)"""


import os
import subprocess
import time

PROCESS = []

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        catalog = os.getcwd()
        p = f'python "{catalog}/server.py"'
        PROCESS.append(subprocess.Popen([
            'gnome-terminal',

            "--",
            "python",
            "./server.py",
            ])
        )
        print(p)
        time.sleep(0.1)
        for i in range(2):
            p = f'python "{catalog}/client.py"  userS{i}'
            PROCESS.append(subprocess.Popen([
                'gnome-terminal',
                "--disable-factory",
            "--",
            "python",
            "./client.py",
                "-m",
                "send",
            ])
            )
            print(p)
            time.sleep(0.1)
        for i in range(1):
            p = f'python "{catalog}/client.py" -m listen -u userL{i}'
            PROCESS.append(subprocess.Popen([
                'gnome-terminal',
                "--disable-factory",
            "--",
            "python",
            "./client.py",
            ])
            )
            print(p)
            time.sleep(0.1)
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            VICTIM.kill()