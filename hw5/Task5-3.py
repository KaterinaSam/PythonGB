# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.

try: 
    with open('GeekBrains\hw5\Data5-3.txt', 'r') as file:
        sumSalary = 0; numWorkers = 0
        while (str1 := file.readline().strip()):
            salary = float(str1.split()[1])
            sumSalary += salary
            numWorkers += 1
            if salary < 20000:
                print(f'{ salary } < 20000 - { str1.split()[0] }')
        if numWorkers:
            print(f'Средняя зарплата: { sumSalary/numWorkers }')
        else:
            print('Пустой файл')
except ValueError:
    print('Неправильное число в файле')
except IndexError:
    print('Отсутствует второй параметр в файле')
except FileNotFoundError:
    print('Файл не существует')