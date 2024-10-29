class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start, stop, step = 1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.pointer = self.start
        print()
        return self

    # def __next__(self):
    #     Error = True
    #     while Error:
    #         try:
    #             self.pointer += self.step
    #             if self.pointer < self.stop:
    #                 return self.pointer
    #             elif self.pointer > self.stop:
    #                 raise StepValueError
    #         except StepValueError:
    #             Error = False
    #             return self.pointer
    # def __next__(self):
    #     self.pointer += self.step
    #     if self.pointer > self.stop:
    #         raise StepValueError('Стоп')
    #     elif self.pointer < self.stop:
    #         return self.pointer
    #     else:
    #         return self.pointer

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
for i in iter3:
    print(i, end=' ')
for i in iter4:
    print(i, end=' ')
for i in iter5:
    print(i, end=' ')