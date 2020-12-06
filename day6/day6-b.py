from itertools import groupby
from collections import Counter


def count_all_answers_in_group(group):
    group_len = len(group)
    counter_sum = Counter()

    for person in group:
        counter = Counter(person)
        counter_sum += counter
    return len([k for k, v in counter_sum.items() if v == group_len])


with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    grouping = groupby(lines, lambda x: x == "")
    groups = [list(group) for k, group in grouping if not k]

    sum_of_counts = 0

    for group in groups:
        sum_of_counts += count_all_answers_in_group(group)

    print(sum_of_counts)
