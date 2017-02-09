def gcd(a, b):
    a,b = abs(a), abs(b)    # a = abs(a), b = abs(b)    5, 6
    while b != 0:           # a = abs(a), b = abs(b)
        a, b = b, a%b       # a = b     , b = a%b
    return a



print(gcd(12345678, 987654321))

def frac(a, b):
    if b!= 0:
        c = gcd(a, b)
        a = a/c
        b = b/c
    return a, b


print('fraction is ', int(frac(25, 5)[0]), '/', int(frac(25, 5)[1]))
