## generate_bar
 言わばHealth Barみたいなやつです。パスタ巻き糞ソースです。<br>
 誰か修正して(?)

## これで何ができるの
 指定した文字でバーを作ります。<br>
 get_bar()で<br>
 ■■■■□□□□□□<br>
 ↑こんな感じのバーを出力します。<br>
 先頭と末尾の文字も指定できます。

# 使い方
```python
# 最大値
num_max = 100
# 現在値
num_now = 35

bar_nums = [
 num_max,
 num_now
]

# バーの長さ
bar_range = 10

# バーの文字
"""
リストの要素数
0, 2, 4 -> 残り
1, 3, 5 -> 空
"""
bar_format = [
    "◀", "◁", # 先頭
    "■", "□", # 中間
    "▶", "▷" # 末尾
 ]

bar = get_bar(bar_nums, bar_range, bar_format)
print(f'{"".join(bar["valid"])}{"".join(bar["invalid"])}')
print(bar["percent"])
get_bar()
```
