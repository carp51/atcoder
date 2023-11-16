from collections import defaultdict


N = int(input())
f = list(map(str, input().split()))
M = int(input())
if M != 0:
    g = list(map(str, input().split()))

check = defaultdict(int)

for i in range(N):
    check[f[i]] = 1
    
for i in range(M):
    if check[g[i]] == 0:
        print("NO")
        exit(0)
        
print("YES")