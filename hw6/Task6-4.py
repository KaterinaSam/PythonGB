# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car(object):
    speed = 0
        
    def __init__(self, color, name, is_police):
        """Конструктор"""
        self.color = color
        self.name = name
        self.is_police = is_police
        
    def go(self):
        print(f'Машина {self.name} поехала')
    def stop(self):
        print(f'Машина {self.name} остановилась')
    def turn(self, str1):
        print(f'Машина {self.name} повернула {str1}')
    def show_speed(self):
        print(f'Скорость машины {self.name}: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!', end=' ')
        print(f'Скорость машины {self.name}: {self.speed}')
    
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!', end=' ')
        print(f'Скорость машины {self.name}: {self.speed}')

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

towncar = TownCar('Черный', 'Мазда', False)
workcar = WorkCar('Белый', 'Тойота', False)
sportcar = SportCar('Зеленый', 'Ферари', False)
policecar = PoliceCar('ГИБДД', 'Шевроле', True)

towncar.speed = 100
workcar.speed = 20
sportcar.speed = 200
policecar.speed = 150

towncar.go()
towncar.turn('налево')
towncar.show_speed()
towncar.stop()

workcar.go()
workcar.turn('направо')
workcar.show_speed()
workcar.stop()

sportcar.go()
sportcar.turn('налево')
sportcar.show_speed()
sportcar.stop()

policecar.go()
policecar.turn('направо')
policecar.show_speed()
policecar.stop()