# ввод числа n, сумма n+nn+nnn 
str = input('Введите не отрицательное целое число > ')
try:
    if int(str) >= 0:
        print('Сумма %d + %d + %d = %d' %(int(str), int(str*2), int(str*3), int(str) + int(str*2) + int(str*3)))
    else:
        print(f'Число: {int(str)} отрицательное')    # можно просто str
except ValueError:
    print(f'Строка: {str} не является целым числом')

print('Конец программы')   