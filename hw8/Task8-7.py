# 7. Реализовать проект «Операции с комплексными числами». 
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag
    
    def __add__(self, other):
        return self._real+other._real, self._imag+other._imag
    
    def __mul__(self, other):
        return self._real*other._real - self._imag*other._imag, self._imag*other._real + self._real*other._imag

c1 = Complex(5, 16)
c2 = Complex(5, -5)
print(c1 + c2)
print(c1 * c2)
print('Проверка:')
c3 = complex(5, 16)
c4 = complex(5, -5)
print(c3 + c4)
print(c3 * c4)