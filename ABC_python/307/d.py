from collections import deque

N = int(input())
S = input()

que = deque()

l_num = 0
cnt = 0

while True:
    if cnt >= N:
        break
    
    if S[cnt] == "(":
        que.append(S[cnt])
        l_num += 1
    elif S[cnt] == ")":
        if l_num > 0:
            while True:
                tmp = que.pop()
                if tmp == "(":
                    break
        else:
            que.append(S[cnt])
        l_num -= 1
        l_num = max(0, l_num)
    else:
        que.append(S[cnt])
        
    cnt += 1
    
print("".join(list(que)))