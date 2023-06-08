bytes_words = [b'class',
             b'function',
             b'method'
             ]
def func(*args):
    for item in args:
        for word in item:
            print(word, ' ', type(word), ' ', len(word))
func(bytes_words)
# b'class'   <class 'bytes'>   5
# b'function'   <class 'bytes'>   8
# b'method'   <class 'bytes'>   6