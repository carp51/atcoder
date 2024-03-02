N = int(input())
S = input()

if S.index("|") < S.index("*") < S.rindex("|"):
    print("in")
else:
    print("out")