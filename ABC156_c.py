n = int(input())
x = list(map(int,input().split()))

x = sorted(x)

sum = 0
for i in x:
    sum += i
p1 = sum // len(x)
p2 = p1+1

ans1 = 0
ans2 = 0
for num in x:
    ans1 += (num-p1)**2
    ans2 += (num-p2)**2
ans = min(ans1,ans2)

print(ans)
