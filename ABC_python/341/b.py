N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
    S, T = map(int, input().split())
    if A[i] >= S:
        quotient = A[i] // S
        A[i + 1] += T * quotient
        A[i] -= S * quotient
        
print(A[-1])