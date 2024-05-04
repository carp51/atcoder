from bisect import bisect_left

N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

ans = 0

cs = [0]

for i in range(M):
    cs.append(cs[-1] + B[i])
    
for i in range(N):
    index = bisect_left(B, P - A[i])
    ans += A[i] * index + cs[index]
    ans += P * (M - index)
    
print(ans)