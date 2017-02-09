lst1 = list()
def divisor(a):
    result = 1
    for i in range(1, a+1):
        if a % i == 0:
            lst1.append(i)
    return lst1

#print(divisor(10))

def uniqueprimes(a):
    result = []
    i = 2
    while i * i <= a:
        if a % i:
            i += 1
        else:
            a //= i
            result.append(i)
    if a > 1:
        result.append(a)
    return result

print(uniqueprimes(50))