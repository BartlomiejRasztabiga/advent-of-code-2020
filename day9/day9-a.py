def get_n_before(_numbers, current_index, n):
    return _numbers[current_index - n:current_index]


def is_sum(_numbers, num):
    found = False
    for _i in _numbers:
        for _j in _numbers:
            if _i == _j:
                continue
            if _i + _j == num:
                found = True
    return found


with open('input.txt') as f:
    numbers = [int(x.strip()) for x in f.readlines()]
    preambule_len = 25
    for i in range(preambule_len, len(numbers)):
        current_number = numbers[i]
        preambule = get_n_before(numbers, i, preambule_len)
        if not is_sum(preambule, current_number):
            print(current_number)
            break
