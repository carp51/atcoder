from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(Q):
    L, R = map(int, input().split())
    
    ans = bisect_right(A, R) - bisect_left(A, L)
    
    print(ans)