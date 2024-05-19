from collections import defaultdict

N = int(input())
S = input()

mod = 998244353

set_S = list(set(S))
set_S.sort()
set_n = len(set_S)

ord_S = [ord(S[i]) - 64 for i in range(N)]
check = defaultdict(int)

for i in range(len(set_S)):
    check[set_S[i]] = (i + 1, 2 ** i)

dp = [[[0] * (10) for _ in range((1 << set_n) + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 1 << set_n):
        if check[S[i - 1]][1] == j:
            dp[i][j][check[S[i - 1]][0] - 1] += 1
            
        for k in range(10):
            if i == N:
                break
            
            dp[i + 1][j][k] += dp[i][j][k]
            if j | check[S[i]][1] == j:
                if dp[i][j][k] != 0:
                    if k == check[S[i]][0] - 1:
                        dp[i + 1][j][k] += dp[i][j][k] % mod
            else:
                dp[i + 1][j | check[S[i]][1]][check[S[i]][0] - 1] += dp[i][j][k] % mod

ans = 0
for d in dp[-1]:
    for j in range(10):
        ans += d[j] % mod
        ans %= mod
    
print(ans % mod)