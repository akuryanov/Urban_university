numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
i = 0
for number in numbers:
    if number > 1:
        if number == 2:
            primes.append(number)
        else:
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                else:
                    is_prime = True
                if is_prime == True:
                    primes.append(number)
                    break
                else:
                    not_primes.append(number)
                    break

print('Primes:', primes)
print('Not primes', not_primes)


