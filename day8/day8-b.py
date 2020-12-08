import copy


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


class Processor:
    def __init__(self, _instructions):
        self.instructions = _instructions
        self.acc = 0
        self.next_instruction_index = 0
        self.loop = False

    def execute(self):
        visited_indexes = set()

        while self.next_instruction_index < len(self.instructions):
            if self.next_instruction_index in visited_indexes:
                self.loop = True
                break
            visited_indexes.add(self.next_instruction_index)

            _instruction = self.instructions[self.next_instruction_index]
            self._handle_instruction(_instruction)

    def _handle_instruction(self, _instruction):
        if _instruction.is_nop():
            self.next_instruction_index += 1
        if _instruction.is_acc():
            self.acc += int(_instruction.arg)
            self.next_instruction_index += 1
        if _instruction.is_jmp():
            self.next_instruction_index += int(_instruction.arg)


with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    instructions = list(map(lambda x: Instruction(x), lines))

i = 0
while True:
    while i < len(instructions):
        instructions_copy = copy.deepcopy(instructions)
        instruction = instructions_copy[i]
        i += 1

        if instruction.is_nop():
            instruction.op = 'jmp'
            break
        elif instruction.is_jmp():
            instruction.op = 'nop'
            break

    processor = Processor(instructions_copy)
    processor.execute()
    if not processor.loop:
        print(processor.acc)
        break
