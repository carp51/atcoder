N, K = map(int, input().split())
A = list(map(int, input().split()))

A = list(set(A))

A.sort()

for i in range(min(K, len(A))):
    if i != A[i]:
        print(i)
        exit()
        
print(i + 1)