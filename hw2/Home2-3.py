winter_list = ["декабрь", "январь", "февраль"]
spring_list = ["март", "апрель", "май"]
summer_list = ["июнь", "июль", "август"]
autumn_list = ["сентябрь", "октябрь", "ноябрь"]

month_dict = {1:"январь", 2:"февраль", 3:"март", 4:"апрель", 5:"май", 6:"июнь", 7:"июль", 8:"август", 9:"сентябрь", 10:"октябрь", 11:"ноябрь", 12:"декабрь"}

print("Введите номер месяца - целое число от 1 до 12>")
try:
    iM = int(input())
except ValueError:
    print("Это не целое число.")
    iM = 0

strM = month_dict.get(iM)
if strM == None:
    print("Я календарь переверну, и снова 3-е сентября...")
else:
    print(strM)
    
if strM in winter_list:
    print("Зима!")
else:    
    if strM in spring_list:
        print("Весна!")
    else:
        if strM in summer_list:
            print("Лето!")
        else:    
            if strM in autumn_list:
                print("Осень!")
