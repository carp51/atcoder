A, B = map(int, input().split())
c = set([1, 2, 3])

if A == B:
    print(-1)
else:
    c.discard(A)
    c.discard(B)
    c = list(c)
    print(c[0])