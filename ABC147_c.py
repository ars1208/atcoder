N = int(input())
A = list()
xy = list()
xy_i = list()
for i in range(N):
    A.append(int(input()))
    for j in range(A[i]):
        xy_j = list(map(int,input().split()))
        xy_i.append(xy_j)
    xy.append(xy_i)
    xy_i = list()

print(N,A,xy)
