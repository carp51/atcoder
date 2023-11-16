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

    return cnt


N, M, Q = map(int, input().split())

connect = [[] for _ in range(M + 1)]
check = [[] for _ in range(M + 1)]

for i in range(Q):
    e, t= map(int, input().split())
    check[t].append(e)

for i in range(1, M):
    connect[i].append(i + 1)

ans = 0

for i in range(1, N + 1):
    ans += BFS(i)

print(ans)