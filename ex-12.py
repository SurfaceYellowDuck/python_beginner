import random

N = random.randint(1, 1000000)
n = 2
degree = 0
while n ** degree <= N:
    print(n ** degree)
    degree += 1
