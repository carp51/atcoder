def f(x1, y1, x2, y2):
    return (x1 - y1) ** 2 + (x2 - y2) ** 2 <= D ** 2


N, D = map(int, input().split())

XY = []

for i in range(N):
    X, Y = map(int, input().split())
    XY.append([X, Y])
    
connect = [[] for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        if f(XY[i][0], XY[j][0], XY[i][1], XY[j][1]):
            connect[i].append(j)

from collections import deque


def BFS(start):
    visited = [False] * (N + 1)

    visited[start] = True
    cnt = 1

    que = deque()
    que.append(start)

    while 0 < len(que):
        now_city = que.popleft()

        for to_city in connect[now_city]:
            if visited[to_city] == False:
                visited[to_city] = True
                cnt += 1
                que.append(to_city)

    return visited

ans = BFS(0)

for i in ans[:N]:
    if i:
        print("Yes")
    else:
        print("No")