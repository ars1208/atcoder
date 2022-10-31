N = int(input())
H = list(map(int,input().split()))

highest = H[0]
ans = 1
for i in range(N):
  if highest < H[i]:
    highest = H[i]
    ans = i+1
print(ans)