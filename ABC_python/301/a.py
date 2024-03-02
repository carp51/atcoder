N = int(input())
S = input()

T, A = 0, 0

for i in S:
    if i == "T":
        T += 1
    elif i == "A":
        A += 1
    
if A != T:
    if A > T:
        print("A")
    else:
        print("T")
else:
    T_cnt = 0
    A_cnt = 0
    for i in S:   
        if i == "T":
            T_cnt += 1
        elif i == "A":
            A_cnt += 1
            
        if T_cnt == T:
            print("T")
            break
        elif A_cnt == A:
            print("A")
            break