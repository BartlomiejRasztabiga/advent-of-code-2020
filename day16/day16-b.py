import math


def parse_field(field):
    name, valid = field.split(':')
    valid = [tuple(map(int, r)) for r in
             (r.split('-') for r in valid.split(' or '))]
    return name, valid


def read_ticket(_ticket):
    return list(map(int, _ticket.split(',')))


with open("input.txt") as f:
    fields, ticket, nearby = f.read().split('\n\n')

    fields = {f[0]: f[1] for f in (parse_field(f) for f in fields.splitlines())}
    ticket = read_ticket(ticket.splitlines()[1])
    nearby = [read_ticket(t) for t in nearby.splitlines()[1:]]


def valid_value(_fields, value):
    return any(r[0] <= value <= r[1] for v in _fields.values() for r in v)


def part2():
    # filter valid tickets
    valid = [t for t in nearby if all(valid_value(fields, n) for n in t)]

    # collect the fields that match the values in every position
    candidates = {}
    for i in range(len(ticket)):
        candidates[i] = set()
        for f, v in fields.items():
            if all(any(r[0] <= t[i] <= r[1] for r in v) for t in valid):
                candidates[i].add(f)

    # reduce every set of candidates to a single field
    names = {}
    while candidates:
        # find the position with a single candidate
        i = next(i for i, s in candidates.items() if len(s) == 1)
        # set the field for the position
        names[i] = next(iter(candidates[i]))
        # remove the field from all other candidates
        del candidates[i]
        for j in candidates:
            candidates[j].discard(names[i])

    return math.prod(n for i, n in enumerate(ticket)
                     if names[i].startswith('departure'))


print(part2())
