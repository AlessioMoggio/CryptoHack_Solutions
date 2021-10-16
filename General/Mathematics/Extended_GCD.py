def extendedGCD(p, q):
    if (p == 0):
        return 0, 1

    x, y = extendedGCD(p % q, q)

    x2 = y - (p // q) * x
    y2 = x

    return x2, y2

print(extendedGCD(26513, 32321))
