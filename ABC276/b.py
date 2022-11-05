N, M = map(int, input().split())
answer = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int,input().split())
  answer[a-1].append(b)
  answer[b-1].append(a)

for i in range(N):
  answer[i].sort()
  if answer[i] == []:
    print(0)
  else:
    print(len(answer[i]), *answer[i])