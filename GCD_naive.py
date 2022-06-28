def gcd(a, b):
    best = 0
    for x in range(1,a+b+1):
        if (a % x == 0) and (b % x == 0):
            best = x
    return best