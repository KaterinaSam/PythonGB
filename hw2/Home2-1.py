# list - различные типы данных
chaos_types_list = ["строка",                           # str 
                    765,                                # int
                    0.1,                                # float 
                    True,                               # bool
                    ["string", 999, 11.32, False],      # list 
                    list(range (10))]                   # list

for i in chaos_types_list:
    print(type(i))                                      # выводит типы данных
    