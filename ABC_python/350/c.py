from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

ans = []
check = defaultdict(int)

for i in range(N):
    check[A[i]] = i
    
for i in range(N):
    if i + 1 != A[i]:
        index = check[i + 1]
        ans.append([i + 1, index + 1])
        check[A[i]], check[i + 1] = check[i + 1], check[A[i]]
        A[i], A[index] = A[index], A[i]
            
print(len(ans))
for a in ans:
    print(*a)