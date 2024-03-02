from bisect import bisect_right
N = int(input())
A = list(map(int, input().split()))

cs = [0]
cs_re = [0]

for i in range(N):
    cs.append(cs[-1] + A[i])
    if i % 2 == 1:
        cs_re.append(cs_re[-1] + A[i] - A[i - 1])
    else:
        cs_re.append(cs_re[i])

Q = int(input())
for i in range(Q):
    ans = 0
    l, r = map(int, input().split())
    tmp_l = bisect_right(A, l)
    tmp_r = bisect_right(A, r)
    
    if tmp_l % 2 == 0:
        ans += A[tmp_l] - l
        
    if tmp_r % 2 == 0:
        ans += r - A[tmp_r - 1]
        tmp_r -= 1
        
    if tmp_r >= len(A):
        tmp_r -= 1
        
    ans += A[tmp_r] - A[tmp_l]
    
    ans -= cs_re[tmp_r + 1] - cs_re[tmp_l + 1]
    
    print(ans)
    