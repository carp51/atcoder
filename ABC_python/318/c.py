N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort()

sumF = sum(F)
ans = sum(F)
cnt = 0

while len(F) > 0:
    tmp = 0
    for i in range(D):
        if len(F) == 0:
            break
        tmp += F.pop()
    
    sumF -= tmp - P
    ans = min(ans, sumF)
   
print(ans) 