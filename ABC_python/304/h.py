"""
2021/02/02
@Yuya Shimizu

Boyer-Moore法
"""

def boyer_moore(text, pattern):
    skip = {}
    cnt = 0
    #パターンの文字に応じたずらしを記録
    for i in range(len(pattern) - 1):
        skip[pattern[i]] = len(pattern) - i -1

    i = len(pattern) - 1    #探索初期値はテキストとパターンの先頭が合うようにしたときの末尾になるように設定

    while i < len(text):
        cnt += 1
        match = True    #patternと一致すると仮定

        for j in range(len(pattern)):
            #patternを順に1文字ずつ比較する
            print( pattern[-1-j], text[i - j])
            if text[i - j] != pattern[-1-j]:
                match = False   #不一致
                break   #探索箇所を次に移行するため，これ以上の探索はしない

        if match:   #すべて一致した ⇒ 発見 ⇒ 探索終了
            return i - len(pattern) + 1 #末尾から探索しているため先頭の位置を返す処理を行う
        if text[i] in skip:
            i += skip[text[i]]    #先ほどの結果から得られた探索箇所をずらす分を足し合わせる
        else:
            i += len(pattern)   #ずらす対象がとくに見当たらなければ，パターンの文字数だけずらす
            
    print(cnt)



if __name__ == '__main__':

    TEXT = 'telescopes-in-space'
    PATTERN = 'spac'

    where = boyer_moore(TEXT, PATTERN)

    if where is not None:
        print(f"{where}\nthat is, you can find '{PATTERN}' by running 'TEXT[{where}: {where}+len(PATTERN)]'")
    else:
        print(f"Failure\nthat is, you can't find '{PATTERN}' in the TEXT")