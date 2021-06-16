# запуск скрипта в терминале: py -u "path\file.py" 23 34 45
from sys import argv
print('argv list:', argv)           # для справки

def salary(*arg):   return float(arg[0][1]) * float(arg[0][2]) + float(arg[0][3]) # первый способ

try:
    print(f'Заработная плата {salary(argv)}')                     # первый способ
    # ниже нечитабельный код? зато в одну строчку :-D             # второй способ (ниже)
    print(f'Заработная плата { (lambda x,y,z: float(x)*float(y)+float(z))(list(argv)[1], list(argv)[2], list(argv)[3]) }') 
except ValueError:
    print(f'Аргументы: {list(argv)[1]} или {list(argv)[2]} или {list(argv)[3]} - не числа') 
except IndexError:
    print('Должно быть 3 числа')        # 4 агумента: 1 - название файла + 3 аргумента