import queue

k = int(input())

queue = queue.Queue()
for i in range(1,10):
    queue.put(i)

for i in range(k):
    x = queue.get()
    if x % 10 != 0:
        l = queue.put(10*x + (x%10) -1)
    l = queue.put(10*x + (x%10))
    if x % 10 != 9:
        l = queue.put(10*x + (x%10) +1)
print(x)
