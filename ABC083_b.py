n, a, b = map(int,input().split())

all_sum = 0
for i in range(n+1):
    if i < 10:
        if i >= a and i <= b:
            all_sum += i
        continue
    i_str = str(i)
    # print(i)
    i_list = [int(num) for num in i_str]
    # print(i_list)
    dig_sum = sum(i_list)
    # print(dig_sum)
    if dig_sum >= a and dig_sum <= b:
        all_sum += i

print(all_sum)
