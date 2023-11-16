N = int(input())
S = input()

flag_1 = False
flag_2 = True

for i in range(N):
    if S[i] == "o":
        flag_1 = True
    elif S[i] == "x":
        flag_2 = False
        
print("Yes" if flag_1 and flag_2 else "No")