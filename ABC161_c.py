n, k = map(int,input().split())

if k >= 2 * n:
    print(n)
    quit()
elif k >= n and k < 2*n:
    print(abs(n-k))
    quit()
else:
    x_b = n%k
    x = abs(x_b - k)
    print(min(x_b,x))
