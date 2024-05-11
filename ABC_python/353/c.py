from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()

mod = 10 ** 8
cnt = 0

for i in range(N):
    cnt += N - bisect_left(A, mod - A[i])
    
for i in range(N):
    if A[i] * 2 >= mod:
        cnt -= 1
       
ans = sum(A) * (N - 1) - mod * cnt // 2
 
print(ans)