S = input()
N = len(S)

flag = True
l_B = 1000
r_B = -1

for i in range(N):
    if S[i] == "B":
        l_B = min(l_B, i + 1)
        r_B = max(r_B, i + 1)
        
if l_B % 2 == r_B % 2:
    flag = False
    
l_R = 1000
r_R = -1
K = -1

for i in range(N):
    if S[i] == "R":
        l_R = min(l_R, i + 1)
        r_R = max(r_R, i + 1)
    elif S[i] == "K":
        K = i + 1
        
if not (l_R < K < r_R):
    flag = False
    
print("Yes" if flag else "No")