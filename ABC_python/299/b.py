from collections import defaultdict


N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

check = defaultdict(list)

for i in range(N):
    check[C[i]].append([R[i], i + 1])
    
if len(check[T]) != 0:
    check[T].sort()
    check[T]
    print(check[T][-1][1])
else:
    check[C[0]].sort()
    print(check[C[0]][-1][1])