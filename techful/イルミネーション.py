from collections import defaultdict


N = int(input())
S = input()

check = defaultdict(int)

for i in range(N):
    check_tmp = defaultdict(int)
    
    for j in range(i, N):
        if check_tmp[S[j]] == 0:
            check[S[i: j + 1]] = 1
            check_tmp[S[j]] = 1
        else:
            break
        
print(len(check))