import generate_bar

if __name__ == '__main__':
    # 最大値
    num_max = 100
    # 現在値
    num_now = 35

    bar_nums = [
     num_now,
     num_max
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

    bar = generate_bar.get_bar(bar_nums, bar_range, bar_format)
    print(f'{"".join(bar["valid"])}{"".join(bar["invalid"])}')
    print(bar["percent"])
