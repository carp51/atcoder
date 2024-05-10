from sortedcontainers import SortedSet, SortedList, SortedDict

L, Q = map(int, input().split())
S = SortedSet([0, L])

for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        S.add(x)
    elif c == 2:
        l, r = S.bisect_left(x) - 1, S.bisect_left(x)
        print(S[r] - S[l])