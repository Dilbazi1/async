
import chardet as chardet

strings = [
    'сетевое программирование',
    'сокет',
    'декоратор',
]
with open('test_file.txt', 'w') as f_n:
     for el_str in strings:
         f_n.write(el_str + '\n')
with open('test_file.txt', 'rb') as f_n:
    print(f'Кодировка: {chardet.detect(f_n.read())["encoding"]}')
with open('test_file.txt', 'r', encoding='raw_unicode_escape') as f_n:
    print(f_n.read())
