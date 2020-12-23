import functools
import math

#
# A = [12, 24, 27, 30, 36]
# x = functools.reduce(math.gcd, A)
# print(x)
A = [6, 8]
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
# res = A[0]
# for i in A[1:]:
#     res = gcd(res, i)
#
# print(res)
x = functools.reduce(lambda a, b: a * b // gcd(a, b), A)
print(x)