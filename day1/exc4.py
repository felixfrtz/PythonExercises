from math import sqrt


def fib(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))


def fibsum(n):
    sum = 0
    for i in range(0,n):
        if fib(i) % 2 == 0:
            sum = sum + fib(i)
    return sum

print(fibsum(4000000))