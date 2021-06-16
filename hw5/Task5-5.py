# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

with open('GeekBrains\hw5\Data5-5.txt', 'w+') as file:
    str1 = ''.join( str(tuple(randint(-100, 100) for _ in range(0,20))).strip('()') )
    str1 = str1.replace(',','')
    file.write(str1)
    file.seek(0)
    str1 = file.read()
    print('Элементы из файла:\n', str1)
    print('Сумма элементов: ', sum( map(int, str1.split()) ))