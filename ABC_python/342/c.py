from collections import defaultdict


N = int(input())
S = list(input())
Q = int(input())

str_list = defaultdict(str)

for i in range(26):
    str_list[chr(i + 97)] = chr(i + 97)


for i in range(Q):
    c, d = map(str, input().split())
    for i, j in str_list.items():
        if j == c:
            str_list[i] = d
    
for i in range(N):
    S[i] = str_list[S[i]]
    
print("".join(S))