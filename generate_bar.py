import math
import tools


def get_bar(nums: dict, bar_range, bar_format):
    valid = math.ceil(nums["now"] / (nums["max"] / bar_range))
    invalid = bar_range - valid
    percent = math.ceil((nums["now"] / nums["max"]) * 100)

    if invalid > bar_range:
        invalid = bar_range

    start_times = 0
    end_times = valid
    valid_bar = tools.add_str(bar_range, start_times, end_times,
                              bar_format["1_valid"],
                              bar_format["2_valid"],
                              bar_format["3_valid"])

    start_times = bar_range - invalid
    end_times = bar_range
    invalid_bar = tools.add_str(bar_range, start_times, end_times,
                                bar_format["1_invalid"],
                                bar_format["2_invalid"],
                                bar_format["3_invalid"])
    return {
        'valid': valid_bar,
        'invalid': invalid_bar,
        'percent': percent
    }


if __name__ == '__main__':
    bar_num_max = tools.input_int("最大値: ")
    bar_num_now = tools.input_int("現在値: ")
    bar_nums = {
        "max": bar_num_max,
        "now": bar_num_now
    }

    bar_range = 10
    while True:
        try:
            typed_bar_range = input("バーの長さ: ")
            if typed_bar_range:
                bar_range = int(typed_bar_range)
            break
        except ValueError:
            continue

    bar_format = {
        "1_valid": "◀",
        "1_invalid": "◁",
        "2_valid": "■",
        "2_invalid": "□",
        "3_valid": "▶",
        "3_invalid": "▷"
    }

    bar = get_bar(bar_nums, bar_range, bar_format)
    print(f'{"".join(bar["valid"])}{"".join(bar["invalid"])}')
    print(bar["percent"])
