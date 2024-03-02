from collections import defaultdict

N, Q = map(int, input().split())

connect = defaultdict(set)

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if B not in connect[A]:
            connect[A].add(B)
    elif T == 2:
        if B in connect[A]:
            connect[A].remove(B)
    else:
        flag = False
        if B in connect[A]:
            if A in connect[B]:
                flag = True

        print("Yes" if flag else "No")