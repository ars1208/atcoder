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
