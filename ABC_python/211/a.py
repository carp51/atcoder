from collections import deque

mod = 10 ** 9 + 7

def BFS(start):
    check = [0] * (N + 10)
    visited = [False] * (N + 1)

    visited[start] = True
    check[start] = 1

    que = deque()
    que.append(start)

    min_dict = [0] * (N + 10)
    min_dict[start] = 1

    while 0 < len(que):
        now_city = que.popleft()

        for to_city in connect[now_city]:
            if visited[to_city] == False:
                visited[to_city] = True
                que.append(to_city)
                min_dict[to_city] += min_dict[now_city] + 1

            if min_dict[to_city] - min_dict[now_city] == 1:
                check[to_city] += check[now_city]

    return check[N]


N, M = map(int, input().split())

connect = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)

ans = 0

try:
    ans = BFS(1)
except:
    ans = 0

print(ans % mod)