n = int(input())
a = list(map(int,input().split()))

cnt = 0
judge = "true"
while True:
    for num in a:
        if num % 2 == 1:
            judge = "false"
    if judge == "false":
        break
    cnt += 1
    a = [num / 2 for num in a]

print(cnt)
