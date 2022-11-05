N = int(input())
P = list(map(int,input().split()))

# listの後ろから順に確認していく
j = N - 2
while P[j] < P[j+1]:
  j -= 1

# 後ろから順に、交換する値を探していく
k = N - 1
while P[j] < P[k]:
  k -= 1

P[j], P[k] = P[k], P[j]
print(*P[:j+1], *P[:j:-1])