# """Модуль file_system"""
#
# # получаем кодировку для файла, с которым работаем
# F_N = open('test.txt', 'w', encoding='utf-8')
# F_N.write('test test test')
# F_N.close()
# print(type(F_N))
#
# # явное указание кодировки при работе с файлом
# with open('test.txt', encoding='utf-8') as f_n:
#     for el_str in f_n:
#         print(el_str, end='')
#
#
# # УЗНАТЬ КОДИРОВКУ ФАЙЛА
# # перекодировать, rb
# # chardet
# # dict -> json -> byte
# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.
import chardet as chardet

strings = [
    'сетевое программирование',
    'сокет',
    'декоратор',
]
with open('test_file.txt','w' ) as f_n:
     for el_str in strings:
         f_n.write(el_str + '\n')
with open('test_file.txt','rb' ) as f_n:
    print(f'Кодировка: {chardet.detect(f_n.read())["encoding"]}')
with open('test_file.txt', 'r', encoding='raw_unicode_escape') as f_n:
    print(f_n.read())
