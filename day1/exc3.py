import string


def encode(n):
    if n < 10:
        return n
    else:
        return string.ascii_uppercase[n-10]


# print(encode(8))

##############################

lst1 = list()
lst2 = list()
lst3 = list()

def to_k(n, k):
    res = n
    while res != 0:
        res = n//k
        mod = n % k
        n = res
        if k > 10:
            mod = encode(mod)
        lst1.append(mod)

    lst2 = lst1[::-1]
    lst3 = ''.join(map(str, lst2))
    return lst3

#print(to_k(31, 16))

###############################

def decode(n):
    if n.isdigit():
        return int(n)
    else:
        a = string.ascii_uppercase.find(n) + 10
        return int(a)

#print(decode('B'))

################################

def from_k(s, k):
    sum = 0
    for i in range(0, len(s)):
        num = s[i]
        if k > 10:
            num = decode(num)
        sum = sum + int(num)*k**(len(s)-i-1)
    return sum

#print(from_k('777', 12))
################################

def convert(k, m, s):
    indec = from_k(s, k)
    inm = to_k(indec, m)
    return inm

print(convert(16, 7,'B48C03'))
