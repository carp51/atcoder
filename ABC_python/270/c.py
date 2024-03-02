import sys
sys.setrecursionlimit(10 ** 6)

flag = False
ans = []


def DFS(pre, now):
    if now == Y:
        global flag
        flag = True
        ans.append(now)

    if not flag:
        ans.append(now)

    for to in connect[now]:
        if to != pre:
            DFS(now, to)

    if not flag:
        ans.pop()



N, X, Y = map(int, input().split())

connect = [[] for _ in range(N + 10)]

for i in range(N - 1):
    U, V = map(int, input().split())
    connect[U].append(V)
    connect[V].append(U)

DFS(-1, X)

print(*ans)