n = int(input())
s = input()

cnt = 0
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if s[i-1] != s[j-1]:
            for k in range(j+1,n+1):
                if s[i-1] != s[k-1]:
                    if s[j-1] != s[k-1]:
                        if k != 2*j - i:
                            cnt += 1
                            # print(i,j,k)

print(cnt)
