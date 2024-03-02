from collections import deque
L, N, M = map(int, input().split())

A = deque()
B = deque()

for i in range(N):
    v, l = map(int, input().split())
    A.append([v, l])
    
for i in range(M):
    v, l = map(int, input().split())
    B.append([v, l])
    
ans = 0
    
while len(A) > 0 and len(B) > 0:
    x = A.popleft()
    y = B.popleft()
    
    min_num = min(x[1], y[1])
    
    if x[0] == y[0]:
        ans += min_num
        
    if x[1] - min_num != 0:
        x[1] -= min_num
        A.appendleft(x)
            
    if y[1] - min_num != 0:
        y[1] -= min_num
        B.appendleft(y)
            
print(ans)