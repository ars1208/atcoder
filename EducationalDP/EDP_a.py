N = int(input())
in_list = list(map(int,input().split()))
dp = list()
diff_1 = list()
diff_2 = list()

# diff_1
for i in range(1,N):
    diff_1.append(abs(in_list[i]-in_list[i-1]))

# diff_2
for i in range(2,N):
    diff_2.append(abs(in_list[i]-in_list[i-2]))

dp.append(0)
dp.append(diff_1[0])
for i in range(2,N):
    dp_diff = min(dp[i-1]+diff_1[i-1],dp[i-2]+diff_2[i-2])
    dp.append(dp_diff)
print(dp[-1])
