N = int(input())

check = []
sum_n = 0

for i in range(N):
    S, C = map(str, input().split())
    C = int(C)
    
    check.append([S, C])
    sum_n += C
    
check.sort()
print(check[sum_n % N][0])
