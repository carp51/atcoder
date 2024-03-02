s = input()
t = input()

ans = -1
 
for i in range(min(len(s), len(t))):
    if s[i] != t[i]:
        print(i + 1)
        exit()

print(len(t))