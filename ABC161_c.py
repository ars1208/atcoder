n, k = map(int,input().split())

if k >= 2 * n:
    print(n)
    quit()

if k >= n and k < 2*n:
    print(abs(n-k))
    quit()

if n > k:
    x_b = n%k
    x = abs(x_b - k)
    print(min(x_b,x))
