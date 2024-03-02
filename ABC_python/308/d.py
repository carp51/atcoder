from collections import deque


def BFS(start):
    visited = [[False] * (W) for _ in range(H)]

    visited[0][0] = True

    que = deque()
    que.append(start)
    
    D = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while 0 < len(que):
        now_city = que.popleft()
        
        if check[now_city[2] % 5] != S[now_city[1]][now_city[0]]:
            continue

        for d in D:
            x, y = now_city[0], now_city[1]
            dx, dy = x + d[0], y + d[1]
            
            if not 0 <= dx < W:
                continue
            
            if not 0 <= dy < H:
                continue
            
            if S[dy][dx] != check[(now_city[2] + 1) % 5]:
                continue
            
            if not visited[dy][dx]:
                que.append([dx, dy, (now_city[2] + 1) % 5])
                visited[dy][dx] = True

    return visited[H - 1][W - 1]


H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]
    
check = ["s", "n", "u", "k", "e"]

ans = 0


ans = BFS([0, 0, 0])

print("Yes" if ans else "No")