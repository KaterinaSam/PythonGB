def fact(n):
    if n == 0:
        yield 1
    fct = 1
    for i in range (1,n+1):
        fct *= i
        yield fct


while not input('\nQ - выход, Enter - продолжить > ').upper()  == 'Q':
    try:
        num = int(input('Введите натуральное число > '))
        if num < 0:
            print('Требуется число 0...n')
        else:
            for el in fact(num):
                print(el, end = ' ')
    except ValueError:
        print('Неправильное число')