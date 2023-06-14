def impossible_byte_types(*args):
    for item in args:
        try:

            eval(f'b"{item}"')


        except SyntaxError:
            print(f'{item } impossible byte types')


words = [
    'attribute',
    'класс',
    'функция',
    'type',
]
impossible_byte_types(*words)

# класс impossible byte types
# функция impossible byte types