N, Y = map(int,input().split())

flag = False
for a in range(N+1):
    for b in range(N+1):
        if a+b <= N:
            x = a * 10000
            y = b * 5000
            z = (N - a - b) * 1000
            if x + y + z > Y:
                continue
            if x + y + z == Y:
                print(a,b,N-a-b)
                flag = True
                break
    if flag:
        break


else:
    print("-1 -1 -1")
