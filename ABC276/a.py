S = input()

answer = -1
for i in range(len(S)):
  if S[i] == "a":
    answer = i + 1
print(answer)