N = int(input())
S = input()

ans = max(S.index("A"), S.index("B"), S.index("C"))

print(ans + 1)