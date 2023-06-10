words = ['разработка',
         'администрирование',
         'protocol',
         'standart', ]


def converter_func(*args):
    for word in args:
        encoded_word = word.encode('utf-8')
        print(encoded_word, '-> ', encoded_word.decode('utf-8'))


converter_func(*words)

# b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0' ->  разработка
# b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5' ->  администрирование
# b'protocol' ->  protocol
# b'standart' ->  standart
