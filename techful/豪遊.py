N, M = map(int, input().split())
m = [int(input()) for _ in range(M)]

ans = []

for bit in range(1 << M): 
    b = [] 
    for i in range(M): 
        if bit & (1 << i): 
            b.append(i + 1) 

    sum_num = 0
    
    for i in b:
        sum_num += m[i - 1]
        
    if sum_num > N:
        continue
    
    ans.append([sum_num, b])
    
ans.sort()
print(*ans[-1][-1])