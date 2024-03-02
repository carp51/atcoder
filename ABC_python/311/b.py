N, D = map(int, input().split())

check = [0] * D

for i in range(N):
    S = input()
    for i in range(D):
        if S[i] == "x":
            check[i] += 1
            
ans = -1
tmp = 0

for c in check:
    if c == 0:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
        
ans = max(ans, tmp)
        
print(ans)