from collections import deque


def BFS(start):
    visited = [-1] * (N + 1)

    visited[start] = len(connect[start]) - 1

    que = deque()
    que.append(start)

    while 0 < len(que):
        now_city = que.popleft()
        flag = False

        for to_city in connect[now_city]:
            if visited[to_city] == -1:
                visited[to_city] = visited[now_city]
                visited[to_city] += len(connect[now_city]) - 1
                que.append(to_city)
                flag = True
                
            if len(connect[now_city]) == 1:
                print(visited[now_city])
            

    return visited


N = int(input())

connect = [[] for _ in range(N + 1)]

for i in range(N - 1):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

ans = BFS(1)

print(ans)