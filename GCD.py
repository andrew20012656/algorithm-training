def gcd(a,b):
    if b == 0:
        return a
    a_new = a % b
    return gcd(b, a_new)