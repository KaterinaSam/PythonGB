# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на русские. 
# Новый блок строк должен записываться в новый текстовый файл.

try: 
    with open('GeekBrains\hw5\Data5-4-1.txt', 'r') as file:
        str1 = file.read()
        print(f'Прочитано из файла:\n{ str1 }')
        
        for el in (_:= {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}):
            str1 = str1.replace(el, _.get(el))

        str1.encode('cp1251')               # преобразование кодировки для открытия в текстовом редакторе windows
        with open('GeekBrains\hw5\Data5-4-2.txt', 'w') as file:
            file.write(str1)
            print(f'Записано в файл:\n{ str1 }')

except FileNotFoundError:
    print('Файл не существует') 