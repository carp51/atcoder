def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def reduce(p, q):
    common = gcd(p, q)
    return (p // common, q // common)


from collections import deque
from collections import defaultdict


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


N = map(int, input().split())

connect = [[] for _ in range(N + 1)]

check = defaultdict(tuple)

for i in range(N - 1):
    s, t, x = map(int, input().split())
    connect[s].append(t)
    connect[t].append(s)
    check[(s, t)] = (x, 1)
    check[(t, s)] = (x, -1)

ans = 0

ans += BFS(1)

print(ans)