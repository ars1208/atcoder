import bisect

N = int(input())
L = list(map(int,input().split()))
L.sort()

cnt = 0
for first in range(N):
    for second in range(first+1,N):
        bnd = bisect.bisect_left(L,L[first]+L[second]) - 1
        dif = bnd - second
        if dif > 0:
            cnt += dif

print(cnt)
