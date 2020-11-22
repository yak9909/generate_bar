

def add_str(last_times: int, start_times: int, end_times: int, first: str, middle: str, last: str):
    result = []
    for x in range(start_times, end_times):
        if x == 0:
            result.append(first)
            continue
        elif x == last_times - 1:
            result.append(last)
            continue
        result.append(middle)

    return result


def input_int(type_message: str):
    while True:
        try:
            return int(input(type_message))
        except ValueError:
            continue
