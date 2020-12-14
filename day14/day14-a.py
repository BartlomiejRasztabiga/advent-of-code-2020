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


def write_1(memory, mask, address, value):
    memory[address] = from_bits(masked_value(to_bits(value), mask))


def run(data, write):
    mask = []
    memory = {}

    for line in data:
        if line[:4] == 'mask':
            mask = parse_bitmask(line)
        else:
            address, value = parse_write(line)
            write(memory, mask, address, value)
    return sum(memory.values())


with open('input.txt') as f:
    lines = list(f.readlines())

print(run(lines, write_1))
