class Horse:
    x_distance = 0
    def __init__(self):
        self.sound = 'Frrr'
    def run(self, dx):
        self.x_distance += dx

class Eagle:
    y_distance = 0
    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        super().__init__()
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().__init__()
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        Horse.__init__(self)
        Eagle.__init__(self)
        return (self.x_distance, self.y_distance)
    def voice(self):
        Horse.__init__(self)
        Eagle.__init__(self)
        print(f'{self.sound}')

p1 = Pegasus()
print(Pegasus.mro())
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()