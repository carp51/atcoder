N = int(input())

ans = ""

while True:
    if N == 1:
        break 
    
    if N % 2 == 0:
        ans += "0"
    else:
        ans += "1"
        
    N //= 2
    
tmp = 0
for i in range(len(ans)):
    if ans[i] == "1":
        break
    
    tmp += 1
        
print(tmp)