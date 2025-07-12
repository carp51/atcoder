from collections import deque

query = deque()
Q = int(input())
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        c, x = q[1], q[2]
        query.append([c, x])
    elif q[0] == 2:
        k = q[1]
        sum_num = 0
        for j in range(len(query)):
            left = query.popleft()
            if left[0] > k:
                sum_num += k * left[1]
                left[0] -= k
                query.appendleft(left)
                break
            else:
                k -= left[0]
                sum_num += left[0] * left[1]
        print(sum_num)