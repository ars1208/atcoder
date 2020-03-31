n = int(input())
d_list = list()
for i in range(n):
    d = int(input())
    d_list.append(d)
d_set = set(d_list)

print(len(d_set))
