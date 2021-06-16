import random
list1 = [random.randint(-5, 5) for _ in range(10)]
print(f'Исходный список:\n{ list1 }')
print(f'Получен список:\n{ [list1[i] for i in range(len(list1)) if list1.count(list1[i]) == 1] }')