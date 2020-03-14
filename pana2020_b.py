h,w = map(int,input().split())

if h*w % 2 == 1 or 0 < h*w % 2 < 1:
    ans = (h*w//2) + 1
else:
    ans = h*w//2

if h > 1 and w == 1:
    ans = 1
elif w > 1 and h == 1:
    ans = 1

print(ans)
