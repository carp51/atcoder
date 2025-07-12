from bisect import bisect_right

D = int(input())
X_2 = [i ** 2 for i in range(0, 2 * 10 ** 6 + 100)]

ans = 10 ** 20

for x_2 in X_2:
    index = bisect_right(X_2, D - x_2)
    ans = min(ans, abs(x_2 + (index - 1) ** 2 - D))
    ans = min(ans, abs(x_2 + index ** 2 - D))
    
print(ans)