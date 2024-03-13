from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AA = []

for i in range(N):
    AA.append(A[i])
    AA.append(A[i] + 1)

for i in range(M):
    AA.append(B[i])
    AA.append(B[i] + 1)
    
A.sort()
B.sort()
AA.sort()

ans = 10 ** 20

for i in range(len(AA)):
    A_count = bisect_right(A, AA[i])
    B_count = len(B) - bisect_left(B, AA[i])
    
    if A_count >= B_count:
        ans = min(ans, AA[i])
        
print(ans)