from collections import defaultdict


def read(fname):
    with open(fname, 'r') as f:
        data = [int(x) for x in f]

    # Charging outlet
    data = [0] + sorted(data)
    # The device
    data.append(data[-1] + 3)

    return data


def solve_part2(data):
    # Number of ways to arrange adapters from i to device is memo[i]
    memo = defaultdict(int)

    # Base case, only one way to add the device
    device = data.pop()
    memo[device] = 1

    for i in reversed(data):
        memo[i] = memo[i + 1] + memo[i + 2] + memo[i + 3]

    return memo[0]


def main():
    data = read("input.txt")
    return solve_part2(data)


if __name__ == "__main__":
    part2 = main()
    print(part2)
