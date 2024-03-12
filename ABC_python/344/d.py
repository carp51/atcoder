INF = 10 ** 20

T = input()
N = int(input())

dp = [[INF] * (len(T) + 1) for i in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    AS = list(map(str, input().split()))
    for j in range(len(T) + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
            
    for j in range(1, int(AS[0]) + 1):
        start = 0
        while True:
            index = T.find(AS[j], start, len(T))
            if index != -1:
                if dp[i - 1][index] != INF:
                    dp[i][index + len(AS[j])] = min(dp[i - 1][index] + 1, dp[i - 1][index + len(AS[j])])
                start = index + 1
                continue
                
            break
            
print(dp[-1][-1] if dp[-1][-1] != INF else -1)
    
            