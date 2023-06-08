words = ['разработка', 'сокет', 'декоратор', ]

online_conveted_words = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                         '\u0441\u043e\u043a\u0435\u0442',
                         '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440', ]


def func(*args):
    for item in args:
        for word in item:
            print(word, ' ', type(word), ' ', len(word))


func(words, online_conveted_words)

# разработка  <class 'str'> 10
# сокет < class 'str'> 5
# декоратор <class 'str'> 9

# разработка <class 'str'> 10
# сокет <class 'str'> 5
# декоратор <class 'str'> 9
