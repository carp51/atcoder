def check_takahashi(S):
  stack = []
  for s in S:
    if s.islower():
      if s in stack:
        return False
      stack.append(s)
    elif s == ')':
      if len(stack)==0:
        return False
      stack.pop()

  return True

print(check_takahashi(input()))