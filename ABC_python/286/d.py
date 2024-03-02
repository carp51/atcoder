#Limited
def partial_sum(A, X):
    dp = [[0]*(X + 1) for _ in range(N)]

    dp[0][0] = 1

    if A[0] <= X:
        dp[0][A[0]] = 1

    for i in range(1, N):
        for j in range(X + 1):
            ref = dp[i - 1][j]  
            if A[i] > j: 
                dp[i][j] = ref
            else:
                ref_back = dp[i - 1][j - A[i]]
                dp[i][j] = ref or ref_back
    
    return dp[N - 1][X]
        

N, X = map(int, input().split())
A = []

for i in range(N):
    a, b = map(int, input().split())

    for j in range(b):
        A.append(a)
    
N = len(A)

print("Yes" if partial_sum(A, X) else "No")
        
        