from decimal import Decimal


N = int(input())

ans = []

for i in range(N):
    A, B = map(str, input().split())
    A = Decimal(A)
    B = Decimal(B)
    ans.append([A / (A + B), -(i + 1)])
    
ans.sort(reverse=True) 

ans_2 = [-i[1] for i in ans]

print(*ans_2)