W, B = map(int, input().split())

S = "wbwbwwbwbwbw" * 1000

for i in range(0, len(S) - W - B):
    w, b = 0, 0
    for j in range(W + B):
        if S[i + j] == "w":
            w += 1
        elif S[i + j] == "b":
            b += 1
    
    if w == W and b == B:
        print("Yes")
        exit()
        
print("No")