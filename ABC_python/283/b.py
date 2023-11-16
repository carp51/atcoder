N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        A[q[1] - 1] = q[2]
    else:
        print(A[q[1] - 1])