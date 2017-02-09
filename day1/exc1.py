
lst1 = list()

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        lst1.append(i)
    i = i + 1

b = sum(lst1)
print(b)
print(lst1)


def alldiv(n):
    for i in range(1,n+1):
        if n % i == 0:
            lst1.append(i)
    return lst1


print(alldiv(10))

