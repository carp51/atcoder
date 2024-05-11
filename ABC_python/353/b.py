from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

q = deque(A)
ans = 0

K_count = K

while len(q) > 0:
    que = q.popleft()
    if K_count < que:
        q.appendleft(que)
        ans += 1
        K_count = K
    else:
        K_count -= que
        
print(ans + 1)