# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('GeekBrains\hw5\Data5-2.txt', 'r') as file:
    txtLines = file.readlines()      # чтение всех строк за один раз (так как маленький файл)
    print(f'Строки из файла, количество строк: { len(txtLines) }\n{ txtLines }\n')                 # выводим лист строк
    for el in enumerate(txtLines):
        print(f'Строка №{ el[0]+1 }, количество слов: { len(el[1].strip().split()) }\n{ el[1].strip() }\n')