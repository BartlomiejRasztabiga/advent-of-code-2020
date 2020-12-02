class PasswordPolicy:
    def __init__(self, line):
        splitted = line.split()
        positions = splitted[0].split('-')

        self.first_pos = int(positions[0]) - 1
        self.second_pos = int(positions[1]) - 1
        self.letter = splitted[1][0]

    def validate(self, password):
        is_on_pos_first = password[self.first_pos] == self.letter
        is_on_pos_second = password[self.second_pos] == self.letter
        if is_on_pos_first and is_on_pos_second:
            return False
        elif is_on_pos_first or is_on_pos_second:
            return True


count = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        policy = PasswordPolicy(line)
        password = line.split()[2]
        if policy.validate(password):
            count += 1

print(count)
