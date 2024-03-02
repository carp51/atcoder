N, L = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(N)]

ans = 10 ** 20

for bit in range(1 << L): 
    check = [[] for _ in range(N + 10)]
    b = [] 
    for i in range(L): 
        if bit & (1 << i): 
            b.append(1) 
        else: 
            b.append(0) 
    
    for i in range(L):
        if b[i] == 0:
            continue
        for j in range(N):
            check[j].append(str(X[j][i]))
            
    check = [check[i] for i in range(N + 10) if len(check[i]) != 0]
    
    if len(check) == 0:
        continue
    
    for i in range(len(check)):
        check[i] = tuple(check[i])
           
    check_set = list(set(check))
    
    if len(check[:N]) == len(check_set):
        ans = min(ans, len(check_set[0]))
     
print(ans)