from collections import Counter


def read(fname):
    with open(fname, 'r') as f:
        data = [int(x) for x in f]

    # Charging outlet
    data = [0] + sorted(data)
    # The device
    data.append(data[-1] + 3)

    return data


def solve_part1(data):
    c = Counter(j - i for i, j in zip(data, data[1:]))

    return c[1], c[3]


def main():
    data = read("input.txt")
    a, b = solve_part1(data)
    return a * b


if __name__ == "__main__":
    part1 = main()
    print(part1)
