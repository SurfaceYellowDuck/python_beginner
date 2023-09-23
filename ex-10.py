import random

n = random.randint(1, 100000)
# n = 7
o = 0
r = 0
for n in range(n):
    status = random.randint(0, 1)
    if status == 1:
        o += 1
    else:
        r += 1
if o > r:
    print(r)
else:
    print(o)
# print(o, r)
