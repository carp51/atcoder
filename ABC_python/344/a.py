S = input()

print(S[:S.find("|")] + S[S.rfind("|") + 1:])