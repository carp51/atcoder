N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1] * D for _ in range(N + 1)] for _ in range(K + 1)]

for i in range(1, K + 1):
    for j in range(1, N + 1):
        for k in range(D):
            dp[i][j][k] = max(dp[i][j - 1][k], dp[i][j][k])
            if dp[i - 1][j - 1][k] != -1:
                index = (dp[i - 1][j - 1][k] + A[j - 1]) % D
                dp[i][j][index] = max(dp[i][j][index], dp[i - 1][j - 1][k] + A[j - 1])
            
            
        if i == 1:
            dp[i][j][A[j - 1] % D] = max(A[j - 1], dp[i][j - 1][A[j - 1] % D])
            
            

print(dp[-1][-1][0])