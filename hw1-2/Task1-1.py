# Для справки модуль keyboard
# pip install keyboard
# examples https://github.com/boppreh/keyboard
# examples https://github.com/boppreh/keyboard/tree/master/examples
# import keyboard
# import time
    #time.sleep(1.0)
    #if keyboard.read_key() == "p":
    #    print("You pressed p")
    #    break
    #if keyboard.is_pressed('esc'):
    #    print("You pressed ESC")
    #    break 

# запросить у пользователя числа и строки, сохранить в переменные вывести на экран

print('Введите переменные:')
while not input('Q - выход, Enter - продолжить > ').upper()  == 'Q':
    str = input('Значение переменной = ')
    if str.count('.') == 1:
        try:
            val = float(str)
            print(f'Число с точкой: {val}')
        except ValueError:
            print(f'Строка: {str}')    
    elif (str.count('-') == 1 and str[1:len(str)].isnumeric()) or str.isnumeric():      #if str.isdigit(): if str.isdecimal()
        val = int(str)
        print(f'Целое число: {val}')
    else:
        print(f'Строка: {str}') 

print('Конец программы')