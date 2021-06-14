while not input('Q - выход, Enter - продолжить > ').upper()  == 'Q':
    str1 = input('Введите сколько км в первый день (число) > ')
    str2 = input('Введите сколько км в последний день (число) > ')
    
    try:
        val1 = float(str1)
        val2 = float(str2)
        if val1 > 0 and val2 > 0:
            i = 1
            while val2 > val1:
                val1 += 0.1*val1
                i += 1
            print(f'Количество дней до результата: {i}')
        else:
            print(f'Числа: {val1} или {val2} не положительные')    
    except ValueError:
        print(f'Строки: {str1} или {str2} - не числа')

print('Конец программы')