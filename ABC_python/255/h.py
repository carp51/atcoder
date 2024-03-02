N, M, K = map(int, input().split())

dp = [[0] * K for _ in range(N)]

for i in range(M):
    dp[0][i] = 1          
    
for i in range(N - 1):
    for j in range(K):
        for k in range(M):
            if k + j + 1 >= K:
                break
            
            dp[i + 1][k + j + 1] += dp[i][j] % 998244353
            dp[i + 1][k + j + 1] %= 998244353
            
            
ans = 0

for i in dp[-1]:
    ans += i % 998244353         
                    
                    
print(ans % 998244353)           