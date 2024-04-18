from collections import defaultdict

S = list(input())
T = input()

s_counter = defaultdict(lambda: [])

for i in range(len(S)):
    s_counter[S[i]].append(i)
    
s_counter["x"].append(10 ** 20)

min_n = -1
for i in range(3):
    flag = False
    if len(s_counter[T[i].lower()]) == 0:
        print("No")
        exit()
    for j in s_counter[T[i].lower()]:
        if min_n < j:
            min_n = j
            flag = True
            break
            
    if not flag:
        print("No")
        exit()

print("Yes")