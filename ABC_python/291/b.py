N  = int(input())
X = list(map(int, input().split()))

X.sort()

ans = 0

for i in range(N, len(X) - N):
    ans += X[i]
    
print(ans / (len(X) - 2 * N))