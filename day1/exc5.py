
def palindrome():
    res = ''
    for i in range(100,999):
        for j in range(100,999):
            result = str(i * j)
            if result == result[::-1]:
                print(result)
                res = result
    return res

print(palindrome())
