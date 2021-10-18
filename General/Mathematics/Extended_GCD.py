def extendedGCD(p, q, loop):
    if (p == 0):
        return 0, 1
    print('loop:', loop, ' p:', p, ' q:', q)
    x, y = extendedGCD(q % p, p, loop+1)
    print('loop:', loop,' x:', x, ' y:', y)
    x2 = y - (q // p) * x
    y2 = x

    return x2, y2

print(extendedGCD(26513, 32321, 1))
