def devider (x,y):
    if y == 0:
        return 'Error'
    return x/y

while not input('Q - выход, Enter - продолжить > ').upper()  == 'Q':
    str1 = input('Введите делимое (число) > ')
    str2 = input('Введите делитель (число) > ')
    try:
        val1 = float(str1)
        val2 = float(str2)
        print(devider(val1,val2))    
    except ValueError:
        print(f'Строки: {str1} или {str2} - не числа')

print('Конец программы')