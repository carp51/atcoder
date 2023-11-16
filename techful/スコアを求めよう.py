from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

check = defaultdict(int)

for i in range(N):
    check[A[i]] = i + 1
    
ans = []

for i in range(N):
    if A[i] == 1:
        ans.append(0)
        continue
    
    tmp = abs(check[A[i] - 1] - (i + 1))
    ans.append(tmp)
    
print(*ans)