str1 = input('Введите значение выручки (число) > ')
str2 = input('Введите значение издержек (число) > ')
str3 = input('Введите численность сотрудников (число) > ')
try:
    val1 = float(str1)
    val2 = float(str2)
    val3 = int(str3)
    if val1 >= 0 and val2 >= 0 and val3 > 0:
        valP = val1 - val2
        if valP > 0:
            print('Прибыль - %5.3f, Рентабельность - %5.3f, Прибыль на сотрудника - %5.3f' %(valP, valP/val1, valP/val3))
        elif valP < 0:
            print('Убыток')
        else:
            print('По нулям, без убытков и без прибыли')
    else:
        print(f'Числа: {val1} или {val2} отрицательные, или {str3} - не положительное')    
except ValueError:
    print(f'Строки: {str1} или {str2} - не числа, или {str3} - не целое число')

print('Конец программы')