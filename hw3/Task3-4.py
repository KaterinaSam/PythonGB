def my_func(x, y):
    if y==0: return 1
    z=x
    for i in range(1, abs(y)): z *= x                     
    if y<0: return 1/z
    else:   return z
    
while not input('Q - выход, Enter - продолжить > ').upper()  == 'Q':
    str1 = input('Введите первое число > ')
    str2 = input('Введите второе число (степень) > ')
    
    try:
        val1 = float(str1)
        val2 = int(str2)
        print(f'Способ 1 - { (lambda x, y: x**y)(val1, val2) }')
        print(f'Способ 2 - { my_func(val1, val2) }')     
    except ValueError:
        print(f'Строки: {str1} или {str2} - неправильные числа и делают неправильный мед')
    except ZeroDivisionError:
        print(f'Числа: {val1} и {val2} - деление на ноль')

print('Конец программы')