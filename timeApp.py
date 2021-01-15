import pygame
import locale
import calendar
import datetime

now = datetime.datetime.now()
s = datetime.datetime.now()
while True:
    pygame.init()
    message = int(input("Введите - 1 календарь, "
                        "Введите - 2 число, "
                        "Введите - 3 время иПропустить дата, "
                        "Введите - 4 таймер, "
                        "Введите - 5 день недели "
                        "Закончить программу - 6: "))

    if message == 1:
        print("Календарь: ")
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        current, c = datetime.datetime.now(), calendar.TextCalendar(0)
        print(c.formatmonth(current.year, current.month))
    if message == 2:
        print("Текущее число: %d" % now.day)
    if message == 3:
        print(now.strftime("%d-%m-%Y %H:%M:%S"))
    if message == 4:
        seconds = int(input("На сколько секунд: "))
        s = datetime.datetime.now()
        while True:
            date = datetime.datetime.now() - s
            print(date)
            if date.seconds == seconds:
                print("Time is gone!")
                s = datetime.datetime.now()
                break
    if message == 5:
        print(now.strftime("%A"))
    if message == 6:
        print("Exit")
        break
