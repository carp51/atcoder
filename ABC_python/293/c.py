import copy
H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]

dp = [[[] for _ in range(W)] for _ in range(H)]

d = [[1, 0], [0, 1]]

dp[0][0].append([A[0][0]])

for h in range(H):
    for w in range(W):
        for i in range(len(dp[h][w])):
            for to in d:
                dx = w + to[0]
                dy = h + to[1]
            
                if not dx < W:
                    continue
            
                if not dy < H:
                    continue
                
                if A[dy][dx] in dp[h][w][i]:
                    continue
                
                to_l = copy.deepcopy(dp[h][w][i])
                to_l.append(A[dy][dx])
                
                dp[dy][dx].append(to_l)
                
print(len(dp[H - 1][W - 1]))
                

            
            