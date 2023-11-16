N, M = map(int, input().split())
A = list(map(int, input().split()))

cs = [0]

for i in range(N):
    cs.append(cs[-1] + A[i])
    
print(cs)