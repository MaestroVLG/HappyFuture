import threading
from time import time, sleep
from threading import Thread

import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies > 0:
            time.sleep(1)
            days += 1
            self.enemies -= self.power
            print(f'{self.name}, сражается {days} день(дня)..., осталось {self.enemies} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print("Все битвы закончились!")






