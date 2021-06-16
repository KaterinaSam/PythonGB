# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# 
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def strCleaner(el:str, alpha:bool):
    s = ''
    for i in range(len(el)):
        if alpha:                       
            if el[i].isalpha():     # в цикле копируем только буквы
                s += el[i]
        else:
            if el[i].isdigit():     # в цикле копируем только цифры
                s += el[i]
    return s

try: 
    with open('GeekBrains\hw5\Data5-6.txt', 'r') as file:
        lessons = {}
        while (str1 := file.readline().strip('().-\n ')):                  
            _str = '';  sum = 0
            for el in enumerate(str1.split()):
                if el[0] == 0:
                    _str = strCleaner(el[1], True)                      # наименование предмета в строку                 
                else:                                                   # после нулевого элемента - числа
                    _s = strCleaner(el[1], False)
                    if len(_s):
                        sum += int( _s )                                # сумма чисел
            _les = {}; _les[_str] = sum                                 # промежуточный словарь
            lessons.update( _les )
        
        print(lessons)            

except FileNotFoundError:
    print('Файл не существует')
except UnicodeDecodeError:                                              # всроенный терминал работает в кодировке символов ОС
    print('Кодировка файла не соотвествует кодировке ОС') 