N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = K * (1 + K) // 2
A = list(set(A))
A.sort()

for a in A:
    if a <= K:
        ans -= a
        
print(ans)