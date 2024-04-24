from collections import defaultdict


N, T = map(int, input().split())

count = 1
check = defaultdict(int)
check[0] = N
scores = [0] * N

ans = []

for i in range(T):
    A, B = map(int, input().split())
    check[scores[A - 1]] -= 1
    scores[A - 1] += B
    
    if check[scores[A - 1]] == 0:
        if check[scores[A - 1] - B] != 0:
            count += 1
    else:
        if check[scores[A - 1] - B] == 0:
            count -= 1
        
    ans.append(count)
        
    check[scores[A - 1]] += 1
    
for i in ans:
    print(i)