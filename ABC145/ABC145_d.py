x, y = map(int,input().split())

mod = 10**9 + 7
n = (2*y - x) // 3 # (+1, +2)
m = (2*x - y) // 3 # (+2, +1)
N = 10**6
g1 = [1,1]
g2 = [1,1]
inverse = [0,1]

def comb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r,n-r)
    return g1[n] * g2[r] * g2[n-r] % mod


if __name__ == '__main__':
    if (x+y) % 3 != 0:
        print(0)
        exit()
    if n < 0 or m < 0:
        print(0)
        exit()
    sum = n + m
    r = min(n,m)

    for i in range(2, N+1):
        g1.append((g1[-1]*i) % mod)
        inverse.append((-inverse[mod%i] * (mod//i)) % mod)
        g2.append((g2[-1]*inverse[-1]) % mod)

    print(comb(sum,r,mod))
