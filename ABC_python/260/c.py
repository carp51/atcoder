from collections import deque, Counter

N = int(input())
a = list(map(int, input().split()))
a.sort()
ql = []
qr = []

dic = dict(Counter(a))
for i, j in dic.items():
    for k in range(j):
        if k == 0:
            ql.append(i)
        else:
            qr.append(i)
            
q = ql + qr
q = deque(q)
        

ans = []

for i in range(N):
    if len(q) == 0:
        break

    que = q.popleft()      
    if que == i + 1:
        ans.append(i + 1)
    else:
        q.appendleft(que)
        if len(q) >= 2:
            ans.append(i + 1)
            q.pop()
            q.pop()
        else:
            break
        
print(len(ans))
