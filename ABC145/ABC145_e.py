import numpy as np


if __name__ == '__main__':
    # input
    N, T = map(int,input().split())
    menu = list()
    for i in range(N):
        menu_i = tuple(map(int,input().split()))
        menu.append(menu_i)
    menu.sort()
    dp = np.zeros(T, int)
    ans = 0
    # print(N,T,menu)

    for ab in menu:
        # print(ab[0],ab[1])
        ans = max(ans, dp[-1]+ab[1])
        dp[ab[0]:] = np.maximum(dp[ab[0]:], dp[:-ab[0]] + ab[1])
    print(ans)
