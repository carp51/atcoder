from collections import defaultdict, Counter

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

check = defaultdict(int)

check[A[0]] = 0

ans = [0 for _ in range(N + 10)]

pre_num = A[0]

for i in range(1, N):
    if A[i] == A[0]:
        continue

    if pre_num != A[i]:
        check[A[i]] = check[pre_num] + 1
        pre_num = A[i]

c = Counter(A)

for i, j in check.items():
    ans[j] = c[i]

for i in range(N):
    print(ans[i])