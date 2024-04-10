N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = 10 ** 20
ans = -1

for i in range(10 ** 6 + 100):
    tmp = INF
    for j in range(N):
        if Q[j] - A[j] * i < 0:
            tmp = -INF
            break
        
        if B[j] != 0:
            tmp = min(tmp, (Q[j] - A[j] * i) // B[j])
    
    ans = max(ans, i + tmp)
    
print(ans)
        