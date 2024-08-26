numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    for j in range(1,len(numbers) - 1):
        if numbers[i] % numbers[j] != 0:
            if numbers[i] % numbers[j+1] != 0:
                continue
            elif numbers[i] / numbers[j+1] == numbers[i] / numbers[i]:
                primes.append(numbers[i])
                break
            else:
                not_primes.append(numbers[i])
                break
        else:
            if numbers[i] == 2:
                primes.append(numbers[i])
                break
            else:
                not_primes.append(numbers[i])
                break
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')


