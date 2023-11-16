H, W = map(int, input().split())
N, M  = map(int, input().split())
S = [list(input()) for _ in range(N)]

canvas = [[0] * W for _ in range(H)]

Q = int(input())

for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    for i in range(N):
        for j in range(M):
            if S[i][j] == "#":
                canvas[y + i][x + j] = (canvas[y + i][x + j] + 1) % 2

for i in range(H):
    for j in range(W):
        if canvas[i][j] == 1:
            canvas[i][j] = "#"
        else:
            canvas[i][j] = "_"
            
for i in canvas:
    print("".join(i))