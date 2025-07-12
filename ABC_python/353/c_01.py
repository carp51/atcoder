from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 8
A.sort()

cnt = 0

for i in range(N):
    tmp = bisect_left(A, mod - A[i])
    cnt += N - bisect_left(A, mod - A[i])
    

    
ans = sum(A) * (N - 1) - cnt * mod

print(ans)