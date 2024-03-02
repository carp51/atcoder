from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

check = defaultdict(lambda: defaultdict(int))

for i in range(N):
    check[i] = check[i - 1].copy()
    check[i][A[i]] += 1

for i in range(Q):
    L, R, X = map(int, input().split())
    print(check[R - 1][X] - check[L - 2][X])
    