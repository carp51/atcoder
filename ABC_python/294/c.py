N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from collections import defaultdict

check = defaultdict(int)

C = A + B

C.sort()

for i in range(len(C)):
    check[C[i]] = i + 1
    
a = [check[A[i]] for i in range(N)]
b = [check[B[i]] for i in range(M)]

print(*a)
print(*b)