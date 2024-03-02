from collections import deque
N, M = map(int, input().split())
a = list(map(int, input().split()))

check = deque()
ans = []

for i in range(1, N + 1):
    if i in a:
        check.append(i)
    else:
        check.append(i)
        while len(check) != 0:
            tmp = check.pop()
            ans.append(tmp)
        
print(*ans)
    
