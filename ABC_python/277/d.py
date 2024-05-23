from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
sum_A = sum(A)

for i in range(N):
    A.append(M + A[i])
    
ans = 10 ** 20
q = deque([-1])
tmp = 0
cnt = 0

for i in range(2 * N):
    que = q.pop()
    cnt += 1
    if A[i] - que <= 1:
        if cnt == N + 1:
            ans = min(ans, sum_A - tmp)
            break
        q.append(que)
        q.append(A[i])
        tmp += A[i] % M
    else:
        q = deque([-1])
        q.append(A[i])
        ans = min(ans, sum_A - tmp)
        tmp = A[i] % M
        cnt = 0
        
print(ans)