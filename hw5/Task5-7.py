# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
# название, форма собственности, выручка, издержки.
# 
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# 
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# 
# Подсказка: использовать менеджеры контекста.

from json import dump

def strCleaner(el:str, alpha:bool):
    s = ''
    for i in range(len(el)):
        if alpha:                       
            if el[i].isalpha():     # в цикле копируем только буквы
                s += el[i]
        else:
            if el[i].isdigit() or el[i] == '.':     # в цикле копируем только цифры
                s += el[i]
    return s

try: 
    with open('GeekBrains\hw5\Data5-7.txt', 'r') as file:
        firmsDict = {}; profitSum = 0; profitCount = 0
        while (str1 := file.readline().strip('().-\n ')):                  
            _str = '';  proceeds = 0; costs = 0
            for el in enumerate(str1.split()):
                if el[0] == 0:
                    _str = strCleaner(el[1], True)                      # наименование предмета в строку                 
                if el[0] == 2:                                          # число - выручка
                    if len(_s := strCleaner(el[1], False)):
                        proceeds = float( _s )
                if el[0] == 3:                                          # число - издержки
                    if len(_s := strCleaner(el[1], False)):
                        costs = float( _s )
            if proceeds - costs > 0:
                profitSum += proceeds - costs
                profitCount += 1
            _prof = {}; _prof[_str] = proceeds - costs                                 # промежуточный словарь
            firmsDict.update( _prof )
        
        profitDict = dict(average_profit = profitSum/profitCount if profitCount else 0)
        
        #resList = []; resList.append(firmsDict); resList.append(profitDict)        # это соотвествует заданию, но JSON-файл
        #print(resList)                                                             # должен оборачиваться в {}, а не в [] 
        
        with open('GeekBrains\hw5\Data5-7.json', 'w') as file:
            firmsDict.update( profitDict )                                          # такой вариант больше похож на JSON-файл
            dump(firmsDict, file)      # dump(resList, file)

except FileNotFoundError:
    print('Файл не существует')