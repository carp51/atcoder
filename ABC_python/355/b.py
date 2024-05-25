N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []

for i in range(N):
    C.append(A[i])
    
for i in range(M):
    C.append(B[i])
    
C.sort()

for i in range(len(C)- 1):
    cnt = 0
    for j in range(2):
        if C[i + j] in A:
            cnt += 1
        
    if cnt == 2:
        print("Yes")
        exit()
        
print("No")