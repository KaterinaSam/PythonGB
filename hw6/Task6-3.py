# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
# оклад и премия, например, {"wage": wage, "bonus": bonus}. 
# Создать класс Position (должность) на базе класса Worker. 
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
# дохода с учетом премии (get_total_income). 
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker(object):
    """
    Работник класс
    """
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}
    def __init__(self, income):
        """Конструктор"""
        self._income = income

class Position(Worker):
    """
    Должность класс
    """
    def get_full_name(self):
        return self.surname + ' ' + self.name
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

pos = Position({"wage": 200000, "bonus": 60000})
pos.surname = 'Иванов'
pos.name = 'Иван'
print(f'Сотрудник {pos.get_full_name()} - доход {pos.get_total_income()}')