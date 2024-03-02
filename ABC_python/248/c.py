N, M, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K):
        for k in range(1, M + 1):
            if j + k > K:  # Kを超える数列はどうでもいいです
                break
            dp[i + 1][j + k] += dp[i][j]
print(dp)