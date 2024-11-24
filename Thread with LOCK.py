import threading
import random
import time
class Bank:
    balance = int()
    lock = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)

    def deposit(self):
        add = Bank.balance
        for i in range(100):
            Bank.balance += random.randint(50, 500)
            time.sleep(0.001)
            if Bank.balance >= 500 and Bank.lock.acquire() == False:
                print(f'Пополнение: {Bank.balance if (Bank.balance - add) == 0 else Bank.balance - add}. Текущий баланс: {Bank.balance}')
                Bank.lock.release()
    def take(self):
        cut = 0
        for i in range(100):
            cut = random.randint(50, 500)
            print(f'Запрос на снятие: {cut}')
            if cut > Bank.balance:
                print(f'На вашем балансе недостаточно средств')
                Bank.lock.acquire()
            else:
                Bank.balance -= cut
                time.sleep(0.001)
                print(f'Снятие: {cut}. Баланс: {Bank.balance - cut}')

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
