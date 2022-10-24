n = int(input())
data_list = list()
for i in range(n):
    data = list(map(int,input().split()))
    data_list.append(data)

t_b = 0
x_b = 0
y_b = 0
ans = "Yes"
for t,x,y in data_list:
    t = t - t_b
    x = abs(x - x_b)
    y = abs(y - y_b)
    # print(t,x,y)
    if (t - (x+y)) % 2 != 0 or t < x+y:
        ans = "No"
        break
    t_b = t
    x_b = x
    y_b = y

print(ans)
