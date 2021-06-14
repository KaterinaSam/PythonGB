rating_list = [7, 5, 3, 3, 2]
print("Начальный рейтинг: ", rating_list)

print ("Введите количество элементов, которые будут добавлены в список рейтинга>")
iNum = int(input())                                            # здесь можно сделать проверку на вводимый тип данных  try - except ValueError

if iNum > 0:                                                        # если количество элементов в будет добавлено больше нуля
    print("Введите элементы рейтинга (натуральные числа)>")
    
    for i in range(0, iNum):
        li = int(input())                                            # вводим элемент, здесь можно сделать проверку на вводимый тип данных  try - except ValueError
        if li > 0:
            try:
                rating_list.index(li)                           # для генерации except
                
                rating_list.reverse()                                   # переворачиваем список, так как index ищет с начала списка  
                rating_list.insert( rating_list.index(li),  li )        # вставляем элемент в начало ряда одинаковых элементов перевернутого списка
                rating_list.reverse()                                   # переворачиваем список обратно
            
            except ValueError:                                  # идентичный элемент не найден
                for j in range(0, len(rating_list)):
                    if li > rating_list[j]:                     # j - это кортеж, где j[0] - индекс элемента, а j[1] - значение элемента 
                        rating_list.insert( j,  li )                     # вставляем элемент слева, так как он больше следующего элемента в списке
                        break;                                   # выходим из цикла
                
                if j == len(rating_list) - 1:                    # дошли до конца списка, но элементов еще не вставили - вставляем в конец (справа)
                        rating_list.insert( j + 1,  li )                     # вставляем элемент в конец списка
        else:
            print("Не натуральное число!")
            #break;
    
    print("Измененный рейтинг: ", rating_list)
