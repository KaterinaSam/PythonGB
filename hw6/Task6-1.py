# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
# третьего (зеленый) — на ваше усмотрение. 
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, 
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
import keyboard
import sys
import signal

def signalHandler(signal, frame):
    print('Выполнение программы прервано')
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)

class TrafficLight(object):
    """
    Светофор класс
    """
    
    def __init__(self, color):
        """Конструктор"""
        if color.lower() == 'желтый' or color.lower() == 'зеленый':
            self.__color = color.lower()
        else:
            self.__color = 'красный'            # иницилизация по-умолчанию: красный цвет светофора
    
    def running(self):
        """ Запуск и переключение светофора """
        print(self.__color)
        if self.__color == 'красный':
            time.sleep(7.0)
            self.__color = 'желтый'
        elif self.__color == 'желтый':
            time.sleep(2.0)
            self.__color = 'зеленый'
        else:
            time.sleep(3.0)
            self.__color = 'красный'
        
        return self.__color

keyboard.add_hotkey('esc', lambda: keyboard.send('ctrl+c'))       # при нажатии на ESC или Ctrl+C - выход изпрограммы

trfLight = TrafficLight('красный')
while True:
    trfLight.running()
