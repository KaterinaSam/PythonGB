# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
# А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
# В базовом классе определить параметры, общие для приведенных типов. 
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    _store = []
        
    def move(self, dev, into = True):
        for el in enumerate(self._store):
            if el[1].get(dev.get_model()):
                el[1].update({dev.get_model():el[1].get(dev.get_model()) + (1 if into else -1)})
                if el[1].get(dev.get_model()) <= 0:
                    self._store.pop(el[0])
                break                       # элемент найден
        else:                               # элемент не найден
            if into:
                self._store.append({dev.get_model():1})
            else:
                return f'Модель "{dev.get_model()}" отсутствует на складе'
        return f'Сделано'

    def __str__ (self):
        s = 'На складе:\n'
        for el in self._store:
            s += f'{str(el)}\n'
        return s

class Device:
    _dev = {}
    def __init__(self, model, brand):
        self._dev['model'] = model
        self._dev['brand'] = brand
        self._dev = self._dev.copy()
    def get_model(self):
        return self._dev.get('model')
    def __str__ (self):
        return f'{self._dev}'

class Printer(Device):
    def __init__(self, model, brand, print_t):
        super().__init__(model, brand)
        self._dev.update({'print_t':print_t})

class Scaner(Device):
    def __init__(self, model, brand, scan_t):
        super().__init__(model, brand)
        self._dev.update({'scan_t':scan_t})

class Copier(Device):
    def __init__(self, model, brand, copy_t):
        super().__init__(model, brand)
        self._dev.update({'copy_t':copy_t})

class StrError(Exception):
    """Ошибка возникает, когда введеные данные не строка"""
    pass
class DevError(Exception):
    """Ошибка возникает, когда введеные данные не соотвествуют типу устройства"""
    pass


storage = Storage()
while (val := input('Введите через ",": тип устройства, модель, бренд, тип исполнения(строка) или "stop" > ')).upper() != 'STOP':
    try:
        str1 = val.replace(' ','')
        data = str1.split(',')
        if data[3].isalpha():
            if data[0] == 'Printer':
                storage.move(Printer(data[1], data[2], data[3]))
            elif data[0] == 'Scaner':
                storage.move(Scaner(data[1], data[2], data[3]))
            elif data[0] == 'Copier':
                storage.move(Copier(data[1], data[2], data[3]))
            else:
                raise DevError
        else:
            raise StrError
    except DevError:
        print(f'Не указан тип устройства')
    except StrError:
        print(f'Тип исполнения: должна быть строка') 
    except IndexError:
        print(f'Данные введены не полностью')

print(storage)