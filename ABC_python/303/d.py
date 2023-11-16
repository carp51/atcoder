X, Y, Z = map(int, input().split())
S = input()

dp = [[10 ** 20, 10 ** 20] for _ in range(len(S) + 1)]

if S[0] == "A":
    dp[0][0] = Y
    dp[0][1] = Z + X
else:
    dp[0][0] = X
    dp[0][1] = Z + Y

for i in range(len(S) - 1):
    for j in range(2):
        for k in range(2):
            tmp = dp[i][j]
            if j != k:
                tmp += Z
            
            if S[i + 1] == "A":
                if k == 0:
                    tmp += Y
                elif k == 1:
                    tmp += X
            else:
                if k == 0:
                    tmp += X
                elif k == 1:
                    tmp += Y
                    
            dp[i + 1][k] = min(dp[i + 1][k], tmp)
            
print(min(dp[len(S) - 1]))
            