import queue
import random
import threading
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def gues_ariival(self, *guest):
        for guest in guests:
            if any(table.guest is None for table in self.tables):
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        guest.start()
                        print(f'{guest.name} сел(-а) за стол номер {table.number}')
                        break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not  None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

            if not self.queue.empty() and any(table.guest is None for table in self.tables):
                guest = self.queue.get()
                for table in self.tables:
                    if table.guest is None:
                        table.guest  = guest
                        guest.start()
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        break

tables = [Table(number) for number in range(1, 6)]

guests_name = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

guests = [Guest(name) for name in guests_name]

cafe = Cafe(*tables)

cafe.gues_ariival(*guests)

cafe.discuss_guests()