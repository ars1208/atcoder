import math

def nPr(n, r):
    ans = 1
    for i in range(r,n+1):
        ans *= i
    return ans

def nCr(n,r):
    nPr(n,r) / math.factorial(r)

n,a,b = map(int,input().split())
ans = 0
num_list = [n for n in range(1,n+1)]
memo = dict()

for i in num_list:
    if i == a or i == b:
        continue

    res = nCr(n,i) % (10**9+7)
    memo[(n,i)] = res
    ans += res
print(ans)
