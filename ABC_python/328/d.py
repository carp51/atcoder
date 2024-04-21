from collections import deque

S = input()
q = deque(["w", "w", "w"])

for i in range(len(S)):
    q.append(S[i])
    tmp = []
    
    if S[i] == "C":
        tmp.append(q.pop())
        tmp.append(q.pop())
        tmp.append(q.pop())
    else:
        continue
        
    if not (tmp[0] == "C" and tmp[1] == "B" and tmp[2] == "A"):
        q.append(tmp[2])
        q.append(tmp[1])
        q.append(tmp[0])
  
q = list(q) 
q = q[3:]  
print("".join(q))