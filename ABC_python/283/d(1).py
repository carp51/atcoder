from collections import defaultdict

S = input()
q = []
check = defaultdict(int)

for i in range(len(S)):
    if S[i] == "(":
        q.append("(")
    elif S[i] == ")":
        while len(q) > 0:
            tmp = q.pop()
            check[tmp] -= 1
            if tmp == "(":
                break
    else:
        if check[S[i]] > 0:
            print("No")
            exit()
        check[S[i]] += 1
        q.append(S[i])
            
print("Yes")