from collections import defaultdict
N = int(input())
S = input()

connect = defaultdict(int)

now_pos = (0, 0)

flag = False

for i in range(N):
    if connect[now_pos] == 1:
        flag = True
        break
        
    connect[now_pos] = 1
    
    now_pos = list(now_pos)
    
    if S[i] == "R":
        now_pos[0] += 1
    elif S[i] == "L":
        now_pos[0] -= 1
    elif S[i] == "U":
        now_pos[1] += 1
    elif S[i] == "D":
        now_pos[1] -= 1
        
    now_pos = tuple(now_pos)
    
if connect[now_pos] == 1:
        flag = True
        
print("Yes" if flag else "No")
    