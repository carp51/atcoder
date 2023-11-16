from collections import deque
Q = int(input())

S = deque()

n = 1
cnt = 1

S.append(1)

for i in range(Q):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        S.append(q[1])
        n = 10 * n + q[1]
        cnt += 1
        n %= 998244353
    elif q[0] == 2:
        tmp = S.popleft()
        cnt -= 1
        n -= tmp * pow(10, cnt, 998244353)
    elif q[0] == 3:
        ans = pow(n, 1, 998244353)
        print(ans)
