class Instruction:
    def __init__(self, string):
        parts = string.split(' ')
        self.op = parts[0]
        self.arg = parts[1]

    def is_nop(self):
        return self.op == 'nop'

    def is_acc(self):
        return self.op == 'acc'

    def is_jmp(self):
        return self.op == 'jmp'

    def __str__(self):
        return f"{self.op} {self.arg}"


with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    instructions = list(map(lambda x: Instruction(x), lines))

acc = 0
i = 0
visited_indexes = set()

while i < len(instructions):
    if i in visited_indexes:
        break
    visited_indexes.add(i)

    instruction = instructions[i]
    if instruction.is_nop():
        i += 1
    if instruction.is_acc():
        acc += int(instruction.arg)
        i += 1
    if instruction.is_jmp():
        i += int(instruction.arg)

print(acc)
