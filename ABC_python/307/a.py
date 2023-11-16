N = int(input())
A = list(map(int, input().split()))

ans = []
cnt = 0


for i in range(N):
    tmp = 0
    for j in range(i * 7, (i + 1) * 7):
        tmp += A[j]
    
    ans.append(tmp)
        
print(*ans)