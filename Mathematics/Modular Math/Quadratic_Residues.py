import math

p = 29
ints = [14, 6, 11]

for i in range(1, p):
    for item in ints:
        if ((pow(i,2) % p) == item):
            print(item, i)