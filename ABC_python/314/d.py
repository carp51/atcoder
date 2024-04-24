N = int(input())
S = list(input())
Q = int(input())

q = []
check = [0, 0]

for i in range(Q):
    que = list(map(str, input().split()))
    q.append(que)
    if que[0] == "2":
        check[0] = i
        check[1] = 2
    
    if que[0] == "3":
        check[0] = i
        check[1] = 3
        
for i in range(Q):
    t, x, c = int(q[i][0]), int(q[i][1]), q[i][2]
    if t == 1:
        S[x - 1] = c
    
    if i == check[0]:
        if check[1] == 2:
            for j in range(N):
                S[j] = S[j].lower()
        elif check[1] == 3:
            for j in range(N):
                S[j] = S[j].upper()
                
print("".join(S))
                