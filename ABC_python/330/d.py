N = int(input())

S = [list(input()) for _ in range(N)]

g = [[0] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            g[i].append(1 + g[i][-1])
        else:
            g[i].append(g[i][-1])
            
r = [[0] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            r[j].append(1 + r[j][-1])
        else:
            r[j].append(r[j][-1])
       
ans = 0    
            
for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            ans += (g[i][-1] - 1) * (r[j][-1] - 1)

print(ans)