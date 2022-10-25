import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)


k = int(input())
sum = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        if gcd(a,b) == 1:
            sum += 1 * k
            continue
        for c in range(1,k+1):
            sum += gcd(a,b,c)

print(sum)

'''
def gcd(p,q):
    if p % q == 0:
        return q
    return gcd(q,p%q)

k = int(input())
sum = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            gcd_1 = gcd(max(a,b),min(a,b))
            sum += gcd(max(gcd_1,c),min(gcd_1,c))
print(sum)
'''
