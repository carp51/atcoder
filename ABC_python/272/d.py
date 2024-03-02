from collections import deque


def BFS(start):
    visited = [[-1] * N for _ in range(N)]

    visited[start[1]][start[0]] = 0

    que = deque()
    que.append(start)

    while 0 < len(que):
        now_pos = que.popleft()
        x, y = now_pos[0], now_pos[1]
        
        for d in move:
            for b in [[1, 1] , [1, -1], [-1, 1], [-1, -1]]:
                dx = x + d[0] * b[0]
                dy = y + d[1] * b[1]
                
                if not (0 <= dx < N):
                    continue
                if not (0 <= dy < N):
                    continue
                
                if visited[dy][dx] == -1:
                    visited[dy][dx] = visited[y][x] + 1
                    que.append([dx, dy])
    return visited


N, M = map(int, input().split())

move = []

for i in range(10 ** 6 + 10):
    if M - (i ** 2) < 0:
        break
    if ((M - (i ** 2)) ** .5).is_integer():
        move.append([i, int((M - (i ** 2)) ** .5)])  

ans = BFS([0, 0])

for i in ans:
    print(*i)