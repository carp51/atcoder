from collections import defaultdict

N, Q = map(int, input().split())

check = defaultdict(int)

num_list = [i for i in range(0, N + 1)]
x = [int(input()) for _ in range(Q)]

for i in range(1, N + 1):
    check[i] = i
    
for i in range(Q):
    if check[x[i]] == N:
        tmp = check[x[i]]
        check[num_list[tmp - 1]] += 1
        check[x[i]] -= 1
        
        num_list[tmp], num_list[tmp - 1] = num_list[tmp - 1], num_list[tmp]
    else:
        tmp = check[x[i]]
        check[num_list[tmp + 1]] -= 1
        check[x[i]] += 1
        
        
        num_list[tmp], num_list[tmp + 1] = num_list[tmp + 1], num_list[tmp]
        
print(*num_list[1:])