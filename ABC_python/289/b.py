N, M = map(int, input().split())
a = list(map(int, input().split()))

check = [False for i in range(N + 10)]

for i in a:
    check[i] = True
    
start = 100000

ans = []
    
for i in range(N + 1):
    if check[i]:
        start = min(i, start)
    else:
        for j in range(i, start - 1, -1):
            ans.append(j)
            
        start = i + 1
        
print(*ans)