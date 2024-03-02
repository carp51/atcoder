from collections import deque
N = int(input())
A = deque(map(int, input().split()))

ans = []

pre_num = A.popleft()

while len(A) > 0:
    tmp = A.popleft()
    
    if pre_num < tmp:
        for i in range(pre_num, tmp):
            ans.append(i)
    else:
        for i in range(pre_num, tmp, -1):
            ans.append(i)
            
    pre_num = tmp
       
ans.append(tmp) 
print(*ans)