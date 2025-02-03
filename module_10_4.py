import threading as tr
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(tr.Thread):
    def __init__(self, name):
        tr.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = Queue()
        self.busy_tables = 0

    def guest_arrival(self, all_guest):
        for guest in all_guest:
            for table in self.tables:
                flag = False
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    flag = True
                    self.busy_tables += 1
                else:
                    if self.busy_tables == 5 and table.number == 5:
                        self.queue.put(guest)
                        print(f'{guest.name} в очереди')
                if flag:
                    break

    def discuss_guests(self):
        while not self.queue.empty() or self.busy_tables > 0:
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        self.busy_tables -= 1
                if not self.queue.empty() and self.busy_tables < 5:
                    if table.guest is None:
                        guest = self.queue.get()
                        table.guest = guest
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        self.busy_tables += 1
                        guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей

guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами

cafe = Cafe(*tables)

# Приём гостей

cafe.guest_arrival(guests)

# Обслуживание гостей

cafe.discuss_guests()
