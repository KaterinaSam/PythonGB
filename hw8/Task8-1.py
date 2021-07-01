# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
# В рамках класса реализовать два метода. 
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, sDate:str, day=0, month=0, year=0):
        """Конструктор"""
        self.__sDate = sDate
        self.__day = day
        self.__month = month
        self.__year = year
        
    @classmethod
    def convert_date(cls, sDate:str):
        day, month, year = map(int, sDate.split('-'))
        return cls(sDate, day, month, year)
        
    @staticmethod
    def check_date(sDate:str):
        day, month, year = map(int, sDate.split('-'))
        return True if 1<=day<=31 and 1<=month<=12 and 1900<=year<=2900 else print('Некорректная дата')
    
    def __str__(self):
        """Вывод в строковом представлении"""
        return f'Дата-строка: {self.__sDate} => дата-числа: {self.__day} - {self.__month} - {self.__year}'

if Date.check_date('01-12-2021'):
    d1 = Date('01-12-2021')
    print('d1 > ', d1)
    d1 = d1.convert_date('01-12-2021')
    print('d1 > ', d1)
if Date.check_date('11-11-2000'):    
    d2 = Date.convert_date('11-11-2000')
    print('d2 > ', d2)
    print('d1 > ', d1)