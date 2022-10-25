n,k = map(int,input().split())

i = 1
cnt = 0
t = 0
while n > 0:
    t = k**i - 1
    i += 1
    cnt += 1
    if n-t <= 0:
        break

print(cnt)
