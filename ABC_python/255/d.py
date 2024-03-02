from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

cs = [0]

for i in range(N):
    cs.append(cs[-1] + A[i])
    
for i in range(Q):
    X = int(input())
    
    ans = 0
    
    l = bisect_left(A, X)
    r = bisect_right(A, X)
    
    ans += abs(cs[l] - X * l)
    
    ans += abs((cs[-1] - cs[l]) - X * (N - l))
    
    
    print(ans)
    
