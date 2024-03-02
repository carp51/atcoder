T = int(input())
for i in range(T):
    N, D, K = map(int, input().split())
    
    if D % N == 0:
        print(K - 1)
        continue
    
    if N % (D % N) != 0:
        ans = ((D % N) * (K - 1)) % N
        print(ans)
    else:
        ans = ((D % N) * (K - 1)) % N
        print(ans + ((K - 1) * (D % N)) // N)