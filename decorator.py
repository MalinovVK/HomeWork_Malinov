def is_prime(func):
    def wrapper(*args):
        l = func(*args)
        k = 0
        for i in range(1,l):
            if l % i == 0:
                k = k + 1
        if k == 2:
            print('Простое')
        else:
            print('Составное')
        return l
    return wrapper
@is_prime
def sum_three(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_

print(sum_three())