import threading as tr
import time as t

class Knight(tr.Thread):
    def __init__(self, name, power):
        tr.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            t.sleep(1)
            if self.enemies >= 0:
                print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} врагов.', end='\n')
            else:
                print(f'{self.name} сражается {self.days} день(дня)..., осталось 0 врагов.', end='\n')
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


# Создание класса

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков и остановка текущего

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения

print('Все битвы закончились!')
