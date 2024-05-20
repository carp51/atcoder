N, K, P = map(int, input().split())
C = []
A = []

inf = 10 ** 20

for i in range(N):
    c, *a = map(str, input().split())
    C.append(int(c))
    A.append(a)

dp = [[inf] * ((P + 1) ** K) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    cost = C[i]
    improvement = A[i]
    for j in range((P + 1) ** K):
        if dp[i][j] == inf:
            continue
        
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        
        status = []
        tmp = j
        for k in range(K):
            status.append(tmp % (P + 1))
            tmp //= (P + 1)
            
        status.reverse()
            
        new_status = []
        for k in range(K):
            new_status.append(min(P, status[k] + int(improvement[k])))
            
        index = 0
        for k in range(K):
            index += new_status[k] * (P + 1) ** (K - k - 1)
            
        dp[i + 1][index] = min(dp[i + 1][index], cost + dp[i][j])
            
print(dp[-1][-1] if dp[-1][-1] != inf else -1)