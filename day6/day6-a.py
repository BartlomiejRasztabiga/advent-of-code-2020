from itertools import groupby


def count_unique_questions_in_group(group):
    return len(set("".join(group)))


with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    grouping = groupby(lines, lambda x: x == "")
    groups = [list(group) for k, group in grouping if not k]

    sum_of_counts = 0

    for group in groups:
        sum_of_counts += count_unique_questions_in_group(group)

    print(sum_of_counts)
