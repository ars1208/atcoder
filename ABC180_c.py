def divisor(n):
    div_list = set()
    i = 1
    while i*i <= n:
        if n%i == 0:
            div_list.add(i)
            div_list.add(n//i)
        i += 1
    div_list = sorted(div_list)
    return(div_list)

n = int(input())
for i in divisor(n):
    print(i)
