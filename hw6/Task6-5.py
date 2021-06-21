# 5. Реализовать класс Stationery (канцелярская принадлежность). 
# Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. 
# Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery(object):
    def __init__(self, title):
        """Конструктор"""
        self._title = title
    
    def draw(self):
        print('Запуск отрисовки')
        
class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self._title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self._title}')
    
class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self._title}')

pen1 = Pen('Parker')
pen2 = Pen('Smith')
pencil = Pencil('Cosmo')
handle = Handle('MarkIt')

pen1.draw()
pen2.draw()
pencil.draw()
handle.draw()