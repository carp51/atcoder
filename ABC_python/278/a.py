N, K = map(int, input().split())
A = list(map(int, input().split()))

if N <= K:
    tmp = [0 for _ in range(N)]
    print(*tmp)
else:
    tmp = []
    for i in range(K, N):
        tmp.append(A[i])

    for i in range(N - len(tmp)):
        tmp.append(0)

    print(*tmp)