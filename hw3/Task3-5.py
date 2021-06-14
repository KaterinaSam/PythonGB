sumValues = 0
while True:
    str1 = input('Введите ряд чисел через пробел > ')
    values = str1.split(' ') #list
    
    try:
        for el in enumerate(values):  sumValues += float(el[1])
        print(f'Сумма текущей итерации - { sumValues }')     
    except ValueError:
        print(f'Строка: {el[1]} - неправильное число и делает неправильный мед')
        break

print(f'Итоговая сумма - { sumValues }')
print('Конец программы')