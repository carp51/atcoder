from collections import deque


def BFS(start, H):
    visited = [False] * (N + 1)

    visited[start] = True
    check[start] = True

    que = deque()
    que.append([start, H])

    while 0 < len(que):
        now_city = que.popleft()
        if now_city[1] <= 0:
            break
        
        new_H = now_city[1]

        now_city = now_city[0]
        for to_city in connect[now_city]:
            if visited[to_city] == False:
                visited[to_city] = True
                check[to_city] = True
                
                que.append([to_city, new_H - 1])

    return


N, M, K  = map(int, input().split())

connect = [[] for _ in range(N + 1)]
keibi = []

check = [False] * (N + 1)

for i in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
    connect[B].append(A)
    
for i in range(K):
    p, h = map(int, input().split())
    BFS(p, h)

ans = 0
for i in range(len(check)):
    if check[i]:
        ans += 1

print(ans)
for i in range(len(check)):
    if check[i]:
        print(i,end=' ')
    