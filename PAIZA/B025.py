from collections import defaultdict

N, M, K = map(int, input().split())
check = defaultdict(lambda: -1)
pos = defaultdict(lambda: -1)

for i in range(M):
    r = int(input())
    check[i] = r - 1
    pos[r - 1] = 1
    
cnt = 0
    
for k in range(K):
    for i in range(M):
        diff_i = check[i]
        for j in range(N):
            diff_i = (diff_i + 1) % N
            if pos[diff_i] == -1:
                pos[check[i]] = -1
                pos[diff_i] = 1
                check[i] = diff_i
            
                cnt += 1
                break
                
                
                
for i in range(M):
    print(check[i] + 1)