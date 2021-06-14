print ("Введите количество товаров в списке>")
iNum = int(input())                                            # здесь можно сделать проверку на вводимый тип данных  try - except ValueError

if iNum > 0:                                                   # если количество товаров в списке будет добавлено больше нуля
    print("Введите характеристики товаров>")
    
    product_list = []
    product_dict = {}
    
    for i in range(0, iNum):
        print(f"{i+1} - товар>")
                                                                # создание словаря с характеристиками
        print("Введите название товара>")
        strVal = input()
        product_dict.update(dict(название = strVal))            
        
        print("Введите стоимость товара>")
        fVal = float(input())
        product_dict.update(dict(цена = fVal))
        
        print("Введите количество товара>")
        iVal = int(input())
        product_dict.update(dict(количество = iVal))
        
        print("Введите единицы измерения товара>")
        strVal = input()
        product_dict.update(dict(ед = strVal))
        
        listVal = []                                            # создаем временный список, чтобы его конвертировать в кортеж
        listVal.append(i+1)
        listVal.append(product_dict.copy())                     # copy требуется, чтобы при изменении product_dict не изменялись элементы в списке
        product_list.append(tuple( listVal ))                   # конвертируем временный список в кортеж, добавляем в конец списка товаров
    
    #print(product_list)    
    print ("[")
    for el in product_list:
        print ("  ", el)
    print ("]")

    product_char_dict = {}
    listName = []
    listPrice = []
    listNum = []
    listNumValue = []
    for el in product_list:
        listVal = list(el);
        product_dict = listVal.pop(1)                           
        
        listName.append(product_dict.get('название'))
        product_char_dict.update(dict(название = listName))
        listPrice.append(product_dict.get('цена'))
        product_char_dict.update(dict(цена = listPrice))
        listNum.append(product_dict.get('количество'))
        product_char_dict.update(dict(количество = listNum))
        listNumValue.append(product_dict.get('ед'))
        product_char_dict.update(dict(ед = listNumValue))
    
    #print(product_char_dict)    
    print ("{")
    for eldict in product_char_dict:
        print (f"   '{eldict}': {product_char_dict.get(eldict)}")
    print ("}")    
