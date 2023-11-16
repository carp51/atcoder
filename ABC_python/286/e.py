from collections import deque
from collections import defaultdict


def BFS(start, goal):
    visited = [-1] * (N + 1)

    visited[start] = 1
    cnt = 0

    check = defaultdict(list)

    check[1].append(start)

    que = deque()
    que.append(start)

    while 0 < len(que):
        now_city = que.popleft()
        if now_city == goal:
            break

        for to_city in connect[now_city]:
            if visited[to_city] == -1:
                visited[to_city] = visited[now_city] + 1
                que.append(to_city)
                check[visited[now_city] + 1].append(to_city)

    for i in check.values():
        tmp = -10
        for j in range(len(i)):
            tmp = max(tmp, A[i[j]])

        cnt += tmp

    if visited[goal] == -1:
        return "Impossible"
    return cnt


N = int(input())

connect = [[] for _ in range(N + 1)]

A = list(map(int, input().split()))

for i in range(N):
    S = input()
    for j in range(len(S)):
        if S[j] == "Y":
            connect[i].append(j)

Q = int(input())

for i in range(Q):
    U, V = map(int, input().split())
    ans = BFS(U - 1, V - 1)
    if ans == "Impossible":
        print("Impossible")
    else:
        print(i + 1, ans)