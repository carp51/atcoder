N, Q = map(int, input().split())

from collections import defaultdict

check = defaultdict(int)

for i in range(Q):
    a, b = map(int, input().split())
    if a == 1:
        check[b] += 1
    elif a == 2:
        check[b] += 2
    else:
        if check[b] >= 2:
            print("Yes")
        else:
            print("No")