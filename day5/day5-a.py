def binary_search(inputs, start, end, upper, ix=0):
    fb = inputs[ix]

    if ix == len(inputs) - 1:
        if fb == upper:
            return start
        else:
            return end

    rang = abs(start - end)

    if fb == upper:
        return binary_search(inputs, start, end - (rang // 2) - 1, upper, ix + 1)
    else:
        return binary_search(inputs, start + (rang // 2) + 1, end, upper, ix + 1)


ids = []

with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    for line in lines:
        FB = line[:7]
        LR = line[7:]
        row = binary_search(FB, 0, 127, 'F')
        col = binary_search(LR, 0, 7, 'L')

        id = row * 8 + col
        ids.append(id)

print(max(ids))
