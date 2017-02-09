from perm import *

# Create a test permutation of length 20
#q = test_permutation(20)
#print(q)
 # Define a permutation of length 10
#p = [1, 2, 3, 0, 5, 4, 6, 7, 8, 9]
p = [1,2,3,0,5,6,4,8,7]
q = [1,2,3,0,5,6,4,8,7]
# print(p)
# print_permutation(p)
# print(is_trivial(p))
# print(p[0])
# print(cycles(p))


def composition(p, q):
    result = []
    for i in q:
        result.append(p[i])
    print(result)
    return print_permutation(result)

print(composition(p, q))

def inverse(p):
    result = []
    for i in p:
        result.append(p.index(i))
        print(result)
    return result

print(inverse(p))