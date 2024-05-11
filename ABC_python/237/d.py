from collections import deque

N = int(input())
S = input()

l = deque([N])

for i in range(N - 1, -1, -1):
    if S[i] == "L":
        l.append(i)
    else:
        l.appendleft(i)
        
print(*l)