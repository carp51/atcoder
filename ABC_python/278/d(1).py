from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

base = -1
add_list = defaultdict(int)

for i in range(Q):
    q, *ix = map(int, input().split())
    if q == 1:
        x = ix[0]
        base = x
        add_list = defaultdict(int)
    elif q == 2:
        i, x = ix[0] - 1, ix[1]
        add_list[i] += x
    elif q == 3:
        i = ix[0] - 1
        if base == -1:
            print(add_list[i] + A[i])
        else:
            print(add_list[i] + base)