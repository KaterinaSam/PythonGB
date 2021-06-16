# запуск скрипта в терминале: py -u "path\file.py" 1 10 5
from sys import argv
print('argv list:', argv)           # для справки

from itertools import count, cycle

try:
    a,b,c = map(int, argv[1:])   # 4 агумента: 1 - название файла + 3 аргумента, поэтому с "1"
    if c <= 0:      print(f'Шаг {c} -> бесконечность')
    else:
        list1 = []
        for i in count(a, c):        # a-start, b - end, c - step 
            if i < b:
                print(i, end =" ")
                list1.append(i)      # формирование списка
            else:
                break
        j = 0
        print(f'\n\n{ list1 }')
        for i in cycle(list1):
            if j < b:
                print(i, end = " ")
                j += 1
            else:
                break
except ValueError:
    print(f'Аргументы: должно быть 3 целых числа')