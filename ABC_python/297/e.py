N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A.append(10 ** 20)

dp = [[-1] * (10 ** 6 + 100) for i in range(N + 1)]

for i in range(N):
    for j in range(1, 10 ** 6):
        if j % A[i] == 0:
            dp[i][j] = 1
            
        if dp[i][j] == 1:
            cnt = 0
            while True:
                if A[i + 1] * cnt + j >= 10 ** 6:
                    break
                dp[i + 1][A[i + 1] * cnt + j] = 1
                cnt += 1
          
          
count = 0      
            
for i in range(len(dp[N - 1])):
    if dp[N - 1][i] == 1:
        count += 1
        
    if count == K:
        print(i)
        break