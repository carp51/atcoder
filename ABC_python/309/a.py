N = int(input())
A = [list(input()) for i in range(N)]

B = [["0"] * N for _ in range(N)]

for i in range(N):
    if i == 0:
        for j in range(N - 1):
            B[i][j + 1] = A[i][j]
        
        B[i + 1][N - 1] = A[i][N - 1]
    elif i == N - 1:
        for j in range(N - 1):
            B[i][j] = A[i][j + 1]
        
        B[i - 1][0] = A[i][0]
    else:
        for j in range(N):
            if j == 0:
                B[i - 1][0] = A[i][0]
            elif j == N - 1:
                B[i + 1][N - 1] = A[i][N - 1]
            else:
                B[i][j] = A[i][j]
                
for b in B:
    print("".join(b))