N = int(input())
A = list(map(int, input().split()))

ans = []

for i in A:
    if i % 2 == 0:
        ans.append(i)
        
print(*ans)