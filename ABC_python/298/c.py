from collections import defaultdict

N = int(input())
Q = int(input())

check = defaultdict(list)
check_h = defaultdict(set)

for i in range(Q):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        check[q[2]].append(q[1])
        check_h[q[1]].add(q[2])
    elif q[0] == 2:
        ans = sorted(check[q[1]])
        print(*ans)
    elif q[0] == 3:
        ans = sorted(list(check_h[q[1]]))
        print(*ans)
    