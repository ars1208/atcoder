N, K = map(int,input().split())
h = list(map(int,input().split()))
dp = list()

dp.append(0)

for i in range(N):
    for j in range(1,K+1):
        dp_diff = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]))
    dp[i] = dp_diff

    # print(dp)
print(dp[-1])
