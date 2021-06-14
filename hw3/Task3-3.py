def my_func(a,b,c,*args):                   # можно передавать разное количество аргументов, минимум - 3
    valMax = max(a,b,c,*args)
    argsTmp = [a,b,c,*args]
    for el in enumerate(argsTmp):
        if el[1] == valMax:
            i = el[0]
            break
    argsTmp.pop(i)
    return valMax + max(argsTmp)
    
while not input('Q - выход, Enter - продолжить > ').upper()  == 'Q':
    str1 = input('Введите первое (число) > ')
    str2 = input('Введите второе (число) > ')
    str3 = input('Введите третье (число) > ')
    
    try:
        val1 = float(str1)
        val2 = float(str2)
        val3 = float(str3)  
        print(my_func(val1,val2,val3))          # можно передавать разное количество аргументов, минимум - 3
    except ValueError:
        print(f'Строки: {str1} или {str2} или {str3} - не числа')

print('Конец программы')