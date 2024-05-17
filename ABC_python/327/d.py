from collections import deque


def BFS(start):
    count = [-1] * (N + 1)
    visited = [False] * (N + 1)

    visited[start] = True
    count[start] = 0
    color[start] = 0

    que = deque()
    que.append(start)
    
    flag = True

    while 0 < len(que):
        now_city = que.popleft()

        for to_city in connect[now_city]:
            if count[now_city] == count[to_city]:
                flag = False
            if visited[to_city] == False:
                visited[to_city] = True
                if count[now_city] == 0:
                    count[to_city] = 1
                    color[to_city] = 1
                else:
                    count[to_city] = 0
                    color[to_city] = 0
                que.append(to_city)

    return flag


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [tuple(sorted([A[i], B[i]])) for i in range(M)]
AB = list(set(AB))
AB.sort()

connect = [[] for _ in range(N + 1)]

for i in range(len(AB)):
    A, B = AB[i][0], AB[i][1]
    connect[A].append(B)
    connect[B].append(A)
    
color = [-1] * (N + 1)
        
for i in range(1, N + 1):
    if color[i] != -1:
        continue
    if not BFS(i):
        print("No")
        exit()
            
print("Yes")