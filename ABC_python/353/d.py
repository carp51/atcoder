N = int(input())
A = list(map(int, input().split()))

mod = 998244353

cs = [0]

for i in range(N):
    cs.append(cs[-1] + A[i])
    
ans = 0

for i in range(1, N):
    ans += A[i] * i + (cs[i] - cs[0]) * 10 ** len(str(A[i]))
    ans %= mod
    
print(ans % mod)