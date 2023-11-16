N = int(input())
S = input()

ans = -1
cnt = 0

if not "-" in S:
    print(-1)
    exit(0)
    
if not "o" in S:
    print(-1)
    exit(0)
    
for i in range(N):
    if S[i] == "o":
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
        
S = list(S)
S.reverse()

cnt = 0    

for i in range(N):
    if S[i] == "o":
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
        
print(ans)