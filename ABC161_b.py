n,m = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a, reverse=True)
all = sum(a)

if a[m-1] >= all / (4*m):
    print("Yes")
else:
    print("No")
