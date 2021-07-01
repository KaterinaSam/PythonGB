# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
# Проверьте его работу на данных, вводимых пользователем. 
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivErr(Exception):
    def __init__(self, val):
        self.__val = val
    def __truediv__(self, other):
        try:
            if float(other.__val) == 0:
                return f'Деление на ноль!'
            return float(self.__val) / float(other.__val)
        except ValueError:
            return f'"{self.__val}" или "{other.__val}" - Не число!'

while not input('\nQ - выход, Enter - продолжить > ').upper()  == 'Q':
    val1 = input('Число: делимое > ')
    val2 = input('Число: делитель > ')
    print( DivErr(val1) / DivErr(val2) )   