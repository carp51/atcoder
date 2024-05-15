import copy
N, K, D = map(int, input().split())
a = list(map(int, input().split()))

dp = [[[0] * D] * (N + 1) for _ in range(K + 1)]

for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = copy.deepcopy(dp[i][j - 1])
        if i == 1:
            dp[i][j][a[j - 1] % D] = max(dp[i][j][a[j - 1] % D], a[j - 1])
            continue
        
        for m in range(D):
            d = a[j - 1]
            
            if dp[i - 1][j - 1][m] == 0:
                continue
            
            dp[i][j][(m + d) % D] = max(dp[i - 1][j - 1][m] + a[j - 1], dp[i][j][(m + d) % D])
            

print("-1" if dp[K][N][0] == 0 else dp[K][N][0])
            
