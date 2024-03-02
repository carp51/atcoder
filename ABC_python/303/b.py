N, M = map(int, input().split())

A = [list(map(int, input().split())) for i in range(M)]

from collections import defaultdict

check = defaultdict(int)

for a in A:
    for j in range(len(a)):
        if j == len(a) - 1:
            continue
        else:
            check[(min(a[j], a[j + 1]), max(a[j], a[j + 1]))] = 1
            
ans = 0          
            
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j > i:
            if check[(i, j)] == 0:
                ans += 1
            
print(ans)