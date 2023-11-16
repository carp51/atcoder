N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

B = []
for i in range(0, P - 1):
    B.append(A[i])
for i in range(R - 1, S):
    B.append(A[i])
for i in range(Q, R - 1):
    B.append(A[i])
for i in range(P - 1, Q):
    B.append(A[i])
for i in range(S, len(A)):
    B.append(A[i])

for b in B:
    print(b, end=' ')