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


def part1():
    return sum(n for t in nearby for n in t if not valid_value(fields, n))


print(part1())
