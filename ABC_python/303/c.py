N, M, H, K = map(int, input().split())
S = input()

xy = [list(map(int, input().split())) for _ in range(M)]

from collections import defaultdict

check = defaultdict(int)

for i in xy:
    check[(i[0], i[1])] = 1

now_pos = [0, 0]

ans = 0

for i in range(len(S)):
    if S[i] == "R":
        now_pos[0] += 1
    elif S[i] == "L":
        now_pos[0] -= 1
    elif S[i] == "U":
        now_pos[1] += 1
    elif S[i] == "D":
        now_pos[1] -= 1
    
    H -= 1
    
    ans += 1
    
    if H < 0:
        break
    
    if check[(now_pos[0], now_pos[1])] == 1:
        if H < K:
            H = K
            check[(now_pos[0], now_pos[1])] = 0
            
if  H == -1:
    print("No")
    exit()
    
print("Yes" if ans >= N else "No")