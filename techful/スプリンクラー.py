N = int(input())
M, L = map(int, input().split())
P = list(map(int, input().split()))

check = [0] * (N + 10)

for i in range(M):
    check[P[i]] += 1
    
    count = 0
    
    while count != L:
        count += 1
        if P[i] + count > N + 1:
            break
        check[P[i] + count] += 1
        
    count = 0
    
    while count != L:
        count += 1
        if P[i] - count < 0:
            break
        check[P[i] - count] += 1
        
ans = 0

for i in check[1:N + 1]:
    if i == 1:
        ans += 1
        
print(ans)