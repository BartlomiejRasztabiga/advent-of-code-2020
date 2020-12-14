def to_bits(n):
    return [int(b) for b in format(n, f'0={36}b')]


def from_bits(bits):
    return int(''.join([str(b) for b in bits]), 2)


def parse_bitmask(bitmask):
    return [None if b == 'X' else int(b) for b in bitmask.strip().split(' = ')[1]]


def parse_write(entry):
    parts = entry.strip().split(' = ')
    address = int(parts[0][4:][:-1])
    value = int(parts[1])
    return address, value


def masked_value(bits, mask):
    return [b if mask[i] is None else mask[i] for i, b in enumerate(bits)]


class TreeNode:
    def __init__(self):
        self.bits = [None, None]
        self.value = 0

    def write_value(self, address, value):
        if len(address) == 0:
            self.value = value
            return

        bit, rest = address[0], address[1:]

        if bit is None:
            self.write_value([0] + rest, value)
            self.write_value([1] + rest, value)
            return

        if self.bits[bit] is None:
            self.bits[bit] = TreeNode()

        self.bits[bit].write_value(rest, value)

    def sum(self):
        return sum([b.sum() for b in self.bits if b is not None]) + self.value


def masked_address(address, mask):
    masked_bit = lambda a, m: a if m == 0 else (1 if m == 1 else None)
    return [masked_bit(a, m) for a, m in zip(address, mask)]


def write_2(memory, mask, address, value):
    memory.write_value(masked_address(to_bits(address), mask), value)


def run(data, write):
    mask = []
    memory = TreeNode()

    for line in data:
        if line[:4] == 'mask':
            mask = parse_bitmask(line)
        else:
            address, value = parse_write(line)
            write(memory, mask, address, value)
    return memory.sum()


with open('input.txt') as f:
    lines = list(f.readlines())

print(run(lines, write_2))
