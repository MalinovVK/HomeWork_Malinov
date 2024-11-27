import random
import threading
import time
import queue

class Table:
    number = int()
    guest = None
    def __init__(self, number):
        self.number = Table.number

class Guest(threading.Thread):
    name = None
    def __init__(self, name):
        threading.Thread.__init__(self)
        Guest.name = self.name
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe:
    q = queue.Queue()
    tables = []
    def __init__(self, *tables):
        Cafe.tables = tables
    def guest_arrival(self, *guests):
        if Table.guest == None:
            Guest.start(self)
            Table.guest = Guest.name
            print(f'{Guest.name}, сел(а) за стол номер {Table.guest}')
        else:
            Cafe.q.get(Guest.name)
            print(f'{Guest.name} в очереди')

    def discuss_guests(self):
        if not Cafe.queue.empty() or Table.guest != None:
            Table.guest.is_alive()
            print(f'{Guest.name} покушал(-а) и ушел(-ла)')
            print(f'Стол номер {Table.number} свободен')
            Table.guest = None
            if Table.guest == None:
                Table.guest = queue.get(Guest.name)
                print(f'{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {Table.number}')
                Guest.start(self)
        else:
            pass

tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
Cafe = Cafe(*tables)
# Приём гостей
Cafe.guest_arrival(*guests)
# Обслуживание гостей
Cafe.discuss_guests()