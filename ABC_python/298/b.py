import copy
N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
B = [list(map(int, input().split())) for i in range(N)]

new_A = copy.deepcopy(A)

for k in range(4):
    flag = True
    for i in range(N):
        for j in range(N):
            if new_A[i][j] == 1:
                if B[i][j] == 0:
                    flag = False
                    
    if flag:
        print("Yes")  
        exit(0)    
                
    for i in range(N):
        for j in range(N):
            new_A[j][N - i - 1] = A[i][j]
            
    A = copy.deepcopy(new_A)
        
print("No")