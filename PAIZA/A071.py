N = int(input())
A = [int(input()) for _ in range(N)]

dp = [[0] * (N + 10) for _ in range(N // 2 + 10)]

for i in range(N // 2 + 1):
    for j in range(i + 1, N + 1):
        if i == 0:
            dp[i][j] = dp[i][j - 1] + A[j - 1]
        else:
            dp[i][j] = max(10 * A[j - 2] + A[j - 1] + dp[i - 1][j - 2], dp[i][j - 1] + A[j - 1])
            
print(dp[N // 2][N])