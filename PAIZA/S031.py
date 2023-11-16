from collections import deque


N, C, K = map(int, input().split())

pipe_list = []

for i in range(N):
    b, p = map(int, input().split())
    pipe_list.append([p, -b])
    
pipe_list.sort()
que = deque()

total_cost = 0
ans = -1

width_list = deque()

for i in range(N):
    que.append(pipe_list[i])
    total_cost += pipe_list[i][0]
    width_list.append(-pipe_list[i][1])
        
    while not (total_cost <= C):
        remove_que = que.popleft()
        width_remove_que = width_list.popleft()
        total_cost -= remove_que[0]
    
    if len(width_list) == K:
        ans = max(ans, min(width_list))
    
print(ans)