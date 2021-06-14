def int_func(s):    return s.title()

while not input('\n Q - выход, Enter - продолжить > ').upper()  == 'Q':
    str1 = input('Введите строки, разделенные пробелом > ')
    strings = str1.split(' ') #list
    for el in enumerate(strings):    print(int_func(el[1]), end=' ')
print('Конец программы')