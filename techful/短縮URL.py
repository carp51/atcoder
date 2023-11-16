from collections import defaultdict


N, M = map(int, input().split())

check = defaultdict(int)

ans = []

for i in range(N):
    dom = input()
    check[dom] = 1
    
for i in range(M):
    url = input()
    
    s_index = [i for i in range(len(url)) if url[i] == "/"]
    
    if len(s_index) == 2:
        dom = url[s_index[1] + 1: len(url)]
    else:
        dom = url[s_index[1] + 1: s_index[2]]
        
    if check[dom] == 1:
        continue
    
    if len(s_index) == 2:
        dom_second = "oooooooooooooooooooooooooooooo"
    else:
        dom_second = url[s_index[2] + 1: len(url)]
        
    if 1 <= len(dom_second) <= 10:
        continue

    for i in dom_second:
        if not  i.isdigit() or i.islower():
            ans.append(url)
            break
       
       
if len(ans) == 0:
    print("NONE")
    exit(0)  
                
for i in ans:
    print(i)
    