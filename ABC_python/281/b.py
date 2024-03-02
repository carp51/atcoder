S = input()

flag = True
count = 0

if len(S) != 8:
    print("No")
    exit(0)

for i in range(len(S)):
    if i == 0 or i == len(S) - 1:
        if not S[i].isupper():
            flag = False
    else:
        if S[i].isdigit():
            count += 1
        else:
            flag = False

if flag:
    tmp = int("".join(S[1: -1]))
    if 100000 <= tmp <= 999999:
        print("Yes")
    else:
        print("No")
else:
    print("No")
