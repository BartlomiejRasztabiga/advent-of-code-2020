class PasswordPolicy:
    def __init__(self, line):
        splitted = line.split()
        occurence_range = splitted[0].split('-')

        self.min = int(occurence_range[0])
        self.max = int(occurence_range[1])
        self.letter = splitted[1][0]

    def validate(self, password):
        count = password.count(self.letter)
        return self.min <= count <= self.max


count = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        policy = PasswordPolicy(line)
        password = line.split()[2]
        if policy.validate(password):
            count += 1

print(count)
