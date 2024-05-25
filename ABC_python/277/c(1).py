from collections import deque, defaultdict


def BFS(start):
    visited = {i: False for i in connect.keys()}

    visited[start] = True
    max_height = 1

    que = deque()
    que.append(start)

    while 0 < len(que):
        now_city = que.popleft()

        for to_city in connect[now_city]:
            if visited[to_city] == False:
                visited[to_city] = True
                max_height = max(max_height, to_city)
                que.append(to_city)

    return max_height

N = int(input())

connect = defaultdict(list)

for i in range(N):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)

ans = BFS(1)

print(ans)