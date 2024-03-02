from collections import defaultdict

N, X = map(int, input().split())
A = list(map(int, input().split()))

check = defaultdict(int)

for i in A:
    check[i] = 1
    
for i in A:
    if check[i + X] == 1:
        print("Yes")
        exit()
        
print("No")