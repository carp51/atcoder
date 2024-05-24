N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-10 ** 20] * (N + 1) for _ in range(M + 1)]
dp[0][0] = 0

for i in range(M + 1):
    for j in range(N):
        dp[i][j + 1] = dp[i][j]
        if i == 0:
            continue
        
        dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j] + i * A[j])
        
print(dp[-1][-1])