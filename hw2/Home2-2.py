user_list = []

print ("Введите количество элементов списка>")
iNum = int(input())                     # здесь можно сделать проверку на вводимый тип данных  try - except ValueError

if iNum > 0:                            # если количество элементов в списке будет больше нуля
    user_list.clear()                   # чистим list
    print ("Введите поочередно элементы списка>")
    i = 0
    while i < iNum:
        print(f"Элемент № {i}>")        # отсчет с нуля
        el = input()                    # вводим элемент
        user_list.append(el)            # добавляем элемент в конец листа
        i += 1
    
    print("Сформирован список: ", user_list)

    if iNum % 2:                        # если нечетное количество элементов - последний не трогаем
        iNum -= 1
    
    i = 0
    while i < iNum:
        user_list[i],user_list[i+1] = user_list[i+1],user_list[i]       # меняем местами соседние элементы
        i += 2

    print("Список изменен: ", user_list)