N, M = map(int, input().split())
a = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for i in range(M):
  ai = a[i]
  graph[ai].append(ai+1)
  graph[ai+1].append(ai)

visited = [False] * (N+1)
ans = []

while False in visited:
  for i in range(1, N+1):
    if visited[i] == False:
      start = i
      break
  stack = [start]
  visited[start] = True
  while len(stack) > 0:
    v = stack.pop()
    ans.append(v)
    for i in graph[v]:
      if visited[i] == False:
        stack.append(i)
        visited[i] = True

print(*ans)