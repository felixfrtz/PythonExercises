def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(fact(28))

def binom(n, k):
    nfac = fact(n)
    kfac = fact(k)
    nkfac = fact(n-k)
    result = nfac / (nkfac * kfac)
    return result


print(binom(12,8))