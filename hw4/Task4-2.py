import random
list1 = [random.randint(-100, 100) for _ in range(0,10)]
print(f'Исходный список:\n{ list1 }')
print(f'Получен список:\n{ [list1[i] for i in range(1, len(list1)) if list1[i] > list1 [i-1]] }')