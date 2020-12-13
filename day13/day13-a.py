from typing import Tuple


def chinese_remainder_gaussian(a, mod_prod, n):
    result = 0
    for i in range(len(n)):
        result += a[i] * mod_prod // n[i] * inverse_mod((mod_prod // n[i]), n[i])
    return result % mod_prod


def inverse_mod(a: int, b: int) -> Tuple[int, int, int]:
    d = b
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return x0 % d


def main(filename: str) -> None:
    with open(filename) as file:
        departure = int(file.readline().strip())
        buses = [int(x) for x in file.readline().split(',') if x != 'x']
    next_bus_time = [bus + departure - (departure % bus) for bus in buses]
    next_bus = next_bus_time.index(min(next_bus_time))
    print(f"Part 1: {buses[next_bus] * (next_bus_time[next_bus] - departure)}")


if __name__ == "__main__":
    main("input.txt")
