N, M = map(int, input().split())

a_list = []

for i in range(M):
    C = int(input())
    
    a = list(map(int, input().split()))
    a_list.append(set(a))
    
cnt = 0

for bit in range(1 << M): 
    b = [] 
    for i in range(M): 
        if bit & (1 << i): 
            b.append(a_list[i]) 

    check = set()
    
    for j in b:
        check = j | check
        
    if len(list(check)) == N:
        cnt += 1
        
print(cnt)
    