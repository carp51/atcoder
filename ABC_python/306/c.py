from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
check = defaultdict(int)

ans = []

for i in range(3 * N):
    if check[A[i]] == 1:
        ans.append([i + 1, A[i]])
        check[A[i]] += 1
    else:
        check[A[i]] += 1
        
ans.sort()

tmp = []

for i in range(len(ans)):
    tmp.append(str(ans[i][1]))
    
print(*tmp)