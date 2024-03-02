N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 2 for _ in range(N + 1)]

for i in range(N):
    if XY[i][0] == 1:
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + XY[i][1])
    else:
        dp[i + 1][0] = max(dp[i][0] + XY[i][1], dp[i][1] + XY[i][1])
        
print(max(dp[-1]))
        