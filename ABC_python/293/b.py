K = int(input())
X = list(map(int, input().split()))

from collections import defaultdict

check = defaultdict(int)

for i in range(K):
    if check[i + 1] == 0:
        check[X[i]] = 1
    else:
        continue
    
ans = []

for i in range(1,K + 1):
    if check[i] == 0:
        ans.append(i)
        
print(len(ans))
print(*ans)