N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 20

if N == 1:
    print(A[0])
    exit()

for bit in range(1 << N - 1): 
    b = [] 
    for i in range(N - 1): 
        if bit & (1 << i): 
            b.append(i) 
    
    if len(b) == 0:
        continue
    
    b.append(100)
    
    cnt = 0
    or_list = []
    or_cal = 0
    for i in range(N):
        if i != b[cnt]:
            or_cal |= A[i]
        else:
            or_cal |= A[i]
            or_list.append(or_cal)
            or_cal = 0
            cnt += 1
            
    or_list.append(or_cal)
    
    xor_cal = 0
    for i in or_list:
        xor_cal ^= i
        
    ans = min(ans, xor_cal)
    
print(ans)
    