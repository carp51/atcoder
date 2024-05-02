N = int(input())
S = list(map(int, input()))
C = list(map(int, input().split()))

dp = [[[0, 0] for _ in range(N + 1)] for j in range(2)]

dp[0][0][1 - S[0]] = C[0]
dp[1][0][S[0]] = C[0]

for i in range(2):
    for j in range(1, N):
        if i == 0:
            dp[i][j][0] = dp[i][j - 1][1]
            dp[i][j][1] = dp[i][j - 1][0]
            dp[i][j][1 - S[j]] += C[j]
        else:
            dp[i][j][0] = dp[i - 1][j - 1][0]
            dp[i][j][1] = dp[i - 1][j - 1][1]
            dp[i][j][1 - S[j]] += C[j]
            
            tmp = [dp[i][j - 1][1], dp[i][j - 1][0]]
            tmp[1 - S[j]] += C[j]
            
            l, r = tmp[0], tmp[1]
            
            dp[i][j][0] = min(dp[i][j][0], l)
            dp[i][j][1] = min(dp[i][j][1], r)
            
print(min(dp[-1][-2]))