def generate_abc_string(k):
    dp = ["ABC"]
    for i in range(1, k):
        prev_string = dp[-1]
        new_string = "A" + prev_string + "B" + prev_string + "C"
        dp.append(new_string)
    return dp[-1]

def get_substring(k, s, t):
    abc_string = generate_abc_string(k)
    return abc_string[s - 1:t]

# kが50の場合、レベル50のABC文字列の1文字目から100文字目を取得
result = get_substring(40, 1, 100)
print(result)
