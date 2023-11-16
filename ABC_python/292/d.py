from collections import deque
from collections import defaultdict


def BFS(start):
    visited = [False] * (N + 1)

    global visited_tmp
    visited_tmp[start] = True
    cnt = 0

    que = deque()
    que.append(start)

    while 0 < len(que):
        now_city = que.popleft()

        for to_city in connect[now_city]:
            if visited[to_city] == False:
                visited_tmp[to_city] = True
                visited[to_city] = True
            
                que.append(to_city)
                
                cnt += check[(min(now_city, to_city), max(now_city, to_city))]

    return cnt


N, M = map(int, input().split())

visited_tmp = [False] * (N + 1)

connect = [[] for _ in range(N + 1)]
check = defaultdict(int)

for i in range(M):
    A, B = map(int, input().split())
    if check[(A, B)] == 0:
        connect[A].append(B)
        connect[B].append(A)
    check[(A, B)] += 1
    check[(B, A)] += 1

ans = 0

for i in range(len(connect)):
    connect[i] = list(set())

for i in range(1, N + 1):
    if not visited_tmp[i]:
        ans += BFS(i)

print(ans)