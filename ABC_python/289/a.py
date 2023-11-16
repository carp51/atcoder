s = list(input())

for i in range(len(s)):
    if s[i] == '0':
        s[i] = "1"
    else:
        s[i] = "0"

print("".join(s))