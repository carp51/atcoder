H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

for i in range(H):
    A.append(A[0])
    A.pop(0)
    for j in range(W):
        A = [list(x) for x in zip(*A)]
        A.append(A[0])
        A.pop(0)
        
        A = [list(x) for x in zip(*A)]
        
        if A == B:
            print("Yes")
            exit()
            
print("No")