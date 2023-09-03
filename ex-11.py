import collections
import itertools
import random


def get_prime_divisors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def calc_product(iterable):
    acc = 1
    for i in iterable:
        acc *= i
    return acc


def get_all_divisors(n):
    primes = get_prime_divisors(n)

    primes_counted = collections.Counter(primes)

    divisors_exponentiated = [
        [div ** i for i in range(count + 1)]
        for div, count in primes_counted.items()
    ]

    for prime_exp_combination in itertools.product(*divisors_exponentiated):
        yield calc_product(prime_exp_combination)


# rand_int = random.randint(1, 100000)
summ = 7
comp = 10
x = 0
y = 0
divisors = get_all_divisors(comp)
for i in divisors:
    if (comp // i) + (comp / (comp // i)) == summ:
        print(comp // i, (comp / (comp // i)))
        break

# print(list(get_all_divisors(40320))) # 8!


