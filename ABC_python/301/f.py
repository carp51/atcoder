from collections import defaultdict

S = input()
T = input()

check_S = defaultdict(int)
check_T = defaultdict(int)

s_num = 0
t_num = 0

atc = ["a", "t", "c", "o", "d", "e", "r"]

for i in range(len(S)):
    if S[i] == "@":
        s_num += 1
    check_S[S[i]] += 1
    
    if T[i] == "@":
        t_num += 1
    check_T[T[i]] += 1
    
for i in range(26):
    i = chr(i + 97)
    if check_S[i] == check_T[i] or i == "@":
        continue
    elif check_S[i] > check_T[i]:
        if not i in atc:
            continue
        t_num -= (check_S[i] - check_T[i])
        check_T[i] += check_S[i] - check_T[i]
    elif check_S[i] < check_T[i]:
        if not i in atc:
            continue
        s_num -= (check_T[i] - check_S[i])
        check_S[i] += check_T[i] - check_S[i]
        
if t_num >= 0 and s_num >= 0:
    for i, j in check_S.items():
        if i =="@":
            continue
        if j != check_T[i]:
            print("No")
            exit()
    
    print("Yes")
else:
    print("No")