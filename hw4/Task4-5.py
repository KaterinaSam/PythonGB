from functools import reduce
from operator import mul

list1 = [el for el in range(100, 1001, 2)] # можно еще так: if el%2==0
print(f'Исходный список:\n{ list1 }')
print(f'Произведение:\n{reduce(lambda x, y: x*y, list1)}') # первый вариант
print(f'Произведение:\n{reduce(mul, list1)}') # второй вариант