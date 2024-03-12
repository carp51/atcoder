from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))
check = defaultdict(int)

for a in A:
    for b in B:
        for c in C:
            check[a + b + c] = 1
            

for i in range(Q):
    if check[X[i]] == 1:
        print("Yes")
    else:
        print("No")