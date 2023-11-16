N, K, D = map(int,input().split())
A = list(map(int,input().split()))
 
l = []

for i in range(N):
    l.append([A[i] % D, A[i]])

l.sort()

dp = [[0] * (N + 1) for i in range(K + 2)]

for i in range(1, K + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if i == 1:
                if l[j - 1][0] == 0:
                    dp[i][j] = l[j - 1][1]
                else:
                    dp[i][j] = dp[i][j - 1]
                
                if k < i:
                    continue
                else:
                    if (l[j - 1][0] + l[k - 1][0]) % D == 0 and k > j:
                        dp[i + 1][k] = dp[i][j]
                    


o = 2