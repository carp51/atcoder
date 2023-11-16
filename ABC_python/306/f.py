import copy
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0], [0, 0]]  for _ in range(N + 1)]

for i in range(N):
    if XY[i][0] == 1:
        dp[i + 1][0][1] = max(dp[i][0][0] + XY[i][1], dp[i][1][0] + XY[i][1])
    else:
        dp[i + 1][0][0] = max(dp[i][0][0] + XY[i][1], dp[i][1][0] + XY[i][1], dp[i][0][1] + XY[i][1], dp[i][1][1] + XY[i][1])
    dp[i + 1][1][1] = max(dp[i][0][1], dp[i][1][1])
    dp[i + 1][1][0] = max(dp[i][0][0], dp[i][1][0])
        
        
print(max(max(dp[-1][0]), max(dp[-1][1])))