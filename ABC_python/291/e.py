from collections import defaultdict, deque

N, M = map(int, input().split())
in_degree = [0] * (N+1)
graph = defaultdict(list)

for _ in range(M):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    in_degree[Y] += 1

# 入次数が0の頂点をキューに入れる
queue = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

# トポロジカルソート
result = []
while queue:
    v = queue.popleft()
    result.append(v)
    for w in graph[v]:
        in_degree[w] -= 1
        if in_degree[w] == 0:
            queue.append(w)

# DAGであれば結果を出力
if len(result) == N:
    print("Yes")
    print(*result)
else:
    print("No")
