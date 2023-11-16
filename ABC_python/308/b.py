from collections import defaultdict

check = defaultdict(lambda: -1)

N, M = map(int, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))

P = list(map(int, input().split()))

for i in range(M):
    check[D[i]] = P[i + 1]
    
ans = 0

for i in range(N):
    if check[C[i]] == -1:
        ans += P[0]
    else:
        ans += check[C[i]]
        
print(ans)