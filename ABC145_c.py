import math

N = int(input())
x = list()
y = list()
sum = 0

def dist(i,j):
    dx = x[i] - x[j]
    dy = y[i] - y[j]
    return math.sqrt(dx*dx + dy*dy)

if __name__ == '__main__':
    for i in range(N):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)

    for i in range(N):
        for j in range(N):
            sum += dist(i,j)

    print(sum/N)
