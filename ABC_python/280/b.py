N = int(input())
S = list(map(int, input().split()))
A = [0] * N
for i in range(N):
    if i == 0:
        A[i] = S[i]
    else:
        A[i] = S[i] - S[i-1]
print(*A)