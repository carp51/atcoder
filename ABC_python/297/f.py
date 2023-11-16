N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()


dp = [[-1] * (10 ** 6 + 100) for i in range(N + 1)]

for i in range(N):
    for j in range(10 ** 6):
        if i == 0:
            if j % A[i] == 0:
                dp[i][j] = 1
        else:
            if j % A[i] == 0:
                dp[i][j] = 1
             
            if dp[i][j] == -1:
                if dp[i - 1][j] == 1:
                    dp[i][j] = 1
                if j - A[i - 1] < 0:
                    continue
                if dp[i - 1][j - A[i - 1]] == 1:
                    dp[i][j] = 1
                    
          
count = -1  
            
for i in range(len(dp[N - 1])):
    if dp[N - 1][i] == 1:
        count += 1
        
    if count == K:
        print(i)
        break
    
print(count)