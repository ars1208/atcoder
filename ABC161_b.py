n,m = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a, reverse=True)
all = sum(a)

cnt = 0
for num in a:
    if num >= all / (4*m):
        cnt += 1
    if cnt >= m:
        print("Yes")
        break
else:
    print("No")
