from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

trap = defaultdict(int)

for i in B:
    trap[i] += 1
    
dp = [False] * (X+1)
dp[0] = True

for i in range(X + 1):
    if dp[i]:
        for a in A:
            if trap[i + a] == 0 and i + a < X + 1:
                dp[i + a] = True
                
            
print("Yes" if dp[-1] else "No")