from collections import deque, defaultdict


def BFS(start):
    max_num = 1
    visited = defaultdict(int)

    visited[1] = 1

    que = deque()
    que.append(start)

    while 0 < len(que):
        now_city = que.popleft()

        for to_city in connect[now_city]:
            if visited[to_city] != 1:
                visited[to_city] = 1
                max_num = max(max_num, to_city)
                que.append(to_city)

    return max_num


N = int(input())

connect = defaultdict(list)

for i in range(N):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)

ans = BFS(1)

print(ans)