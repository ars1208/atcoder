import math

n = int(input())
x = list(map(int,input().split()))

l1 = 0
ecd = 0
cbs = 0

for num in x:
    l1 += abs(num)

for num in x:
    ecd += num**2
ecd = math.sqrt(ecd)

max_num = abs(x[0])
for num in x:
    cbs = max(abs(num),max_num)
    max_num = cbs

print(l1)
print(ecd)
print(cbs)