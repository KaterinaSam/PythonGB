str = input('Введите целое не отрицательное число > ')
try:
    val = int(str)
    if val >= 0:
        valMax = 0
        while val:
            if val %10 > valMax:
                valMax = val %10 
            val //= 10
        print(f'Цифра: {valMax} наибольшая')
    else:
        print(f'Число: {val} отрицательное')    
except ValueError:
    print(f'Строка: {str} не является целым числом')

print('Конец программы') 