Q = int(input())

S = "1"
cnt = 0

for i in range(Q):
    q = list(map(int, input().split()))
    
    if q[0] == 1:
        S += str(q[1])
    elif q[0] == 2:
        S = S[1:]
    elif q[0] == 3:
        ans = pow(int(S), 1, 998244353)
        print(ans)
        
    S = str(pow(int(S), 1, 998244353))
