N = int(input())
A = list(map(int, input().split()))

cs = [0]

for i in range(N):
    cs.append(cs[-1] + A[i])
    

    
for d in range(1, N + 1):
    sum_num = 0
    for i in range(N - d):
        print(9)