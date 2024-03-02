S = input()

from collections import defaultdict
check = defaultdict(int)

num = [[]]
count = 0

for i in range(len(S)):
    if S[i] == "(":
        num.append([])
        count += 1
    elif S[i] == ")":
        for i in num[count]:
            check[i] -= 1
        
        count -= 1
    else:
        if check[S[i]] != 0:
            print("No")
            exit()
        check[S[i]] += 1
        num[count].append(S[i])

print("Yes")
