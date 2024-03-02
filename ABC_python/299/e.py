from collections import deque


def BFS(start, d, ans):
    if d == 0:
        return ans
    
    visited = [False] * (N + 1)
    
    ans = list(ans)

    visited[start] = True

    que = deque()
    que.append([start, 0])

    while 0 < len(que):
        now_city = que.popleft()
        
        if now_city[1] >= d:
            break
        
        ans[now_city[0] - 1] = "0"

        for to_city in connect[now_city[0]]:
            if visited[to_city] == False:
                visited[to_city] = True
                que.append([to_city, now_city[1] + 1])

    return "".join(ans)


N, M = map(int, input().split())

connect = [[] for _ in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

ans = "1" * N

K = int(input())

pd = []

for i in range(K):
    p, d = map(int, input().split())
    pd.append([p, d])
    ans = BFS(p, d, ans)


def check_BFS(start, d, ans):
    visited = [False] * (N + 1)

    visited[start] = True

    que = deque()
    que.append([start, 0])

    while 0 < len(que):
        now_city = que.popleft()
        
        if now_city[1] > d:
            break
        
        if ans[now_city[0] - 1] == "1":
            return True

        for to_city in connect[now_city[0]]:
            if visited[to_city] == False:
                visited[to_city] = True
                que.append([to_city, now_city[1] + 1])

    return False

flag = True

for i in pd:
    p, d = i[0], i[1]
    if not check_BFS(p, d, ans):
        flag = False
    
if flag:
    print("Yes")
    print(ans)
else:
    print("No")
    