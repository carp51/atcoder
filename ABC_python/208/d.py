INF = 10 ** 18

N, M = map(int, input().split())

d = [[INF] * N for _ in range(N)]

for i in range(M):
    A, B, C = map(int, input().split())
    d[A - 1][B - 1] = C
        
ans = 0

for k in range(N):              #経由する頂点
    for i in range(N):          #始点
        for j in range(N):      #終点
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
            
            if d[i][j] != INF and i != j:
                ans += d[i][j]
            
print(ans)

