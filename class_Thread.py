import threading
import time
lock = threading.Lock()
class Knight(threading.Thread):
    days = 0
    counts = 100
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        counts = 100
        days = 0
        with lock:
            while counts != 0:
                time.sleep(1)
                days+=1
                counts -= self.power
                print(f'{self.name} сражается {days} дней, осталось {counts} врагов')
        print(f'{self.name} одержал победу спустя {days} дней')
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()