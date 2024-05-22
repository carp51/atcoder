N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = -10 ** 20
temp = 0

cs = [0]

for i in range(N):
    cs.append(cs[-1] + A[i])

for i in range(N):
    if i < M:
        temp += A[i] * (i + 1)
    else:
        ans = max(ans, temp)
        temp += A[i] * M
        temp -= cs[i] - cs[i - M]
        
ans = max(ans, temp)

print(ans)     