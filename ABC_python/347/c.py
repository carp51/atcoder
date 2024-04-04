N, A, B = map(int, input().split())
D = list(map(int, input().split()))

cs = []
cs1 = []

for i in range(N):
    cs.append(D[i] % (A + B))
    cs1.append(D[i] % (A + B))
    cs.append(D[i] % (A + B) + (A + B))
        
cs = list(set(cs))
cs1 = len(list(set(cs1)))
cs.sort()

for i in range(len(cs) - cs1 + 1):
    if cs[i + cs1 - 1] - cs[i] + 1 <= A:
        print("Yes")
        exit()
        
print("No")