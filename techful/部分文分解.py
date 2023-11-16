def is_palindrome(s):
    return s == s[::-1]

N, Q = map(int, input().split())
S = input()

for i in range(Q):
    l, r = map(int, input().split())
  
    substr = S[l-1:r]

    if is_palindrome(substr):
        print("Yes")
    else:
        print("No")