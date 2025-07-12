from bisect import bisect_left
from collections import deque

N = int(input())
A = list(map(int, input().split()))
A.sort()
que = deque()

mod = 10 ** 8
cnt = 0
pairs_sum = 0

left, right = 0, N - 1

for i in range(N):
    cnt += N - bisect_left(A, mod - A[i])
    
while left < right:
    if A[left] + A[right] >= mod:
        pairs_sum += right - left
        right -= 1
    else:
        left += 1
        
    
    
       
ans = sum(A) * (N - 1) - mod * pairs_sum
 
print(ans)

