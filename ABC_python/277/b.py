N = int(input())
S = [input() for _ in range(N)]

check = ["H", "D", "C", "S"]

check_2 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

flag = True

dic = {}

for i in range(N):
    if S[i][0] not in check:
        flag = False
    
    if S[i][1] not in check_2:
        flag = False
    
    dic.setdefault(S[i], 0)
    dic[S[i]] += 1

for i in dic.values():
    if i != 1:
        flag = False

print("Yes" if flag else "No")