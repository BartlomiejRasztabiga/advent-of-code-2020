import re


class Passport:
    def __init__(self, string):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

        self._parse(string)

    def _parse(self, string):
        components = string.split()
        for component in components:
            after_split = component.split(':')
            key = after_split[0]
            value = after_split[1]
            self._set_component(key, value)

    def _set_component(self, key, value):
        if key == 'byr':
            self.byr = value
        elif key == 'iyr':
            self.iyr = value
        elif key == 'eyr':
            self.eyr = value
        elif key == 'hgt':
            self.hgt = value
        elif key == 'hcl':
            self.hcl = value
        elif key == 'ecl':
            self.ecl = value
        elif key == 'pid':
            self.pid = value
        elif key == 'cid':
            self.cid = value

    def is_valid(self):
        if not self._is_byr_valid():
            return False
        elif not self._is_iyr_valid():
            return False
        elif not self._is_eyr_valid():
            return False
        elif not self._is_hgt_valid():
            return False
        elif not self._is_hcl_valid():
            return False
        elif not self._is_ecl_valid():
            return False
        elif not self._is_pid_valid():
            return False
        return True

    def _is_byr_valid(self):
        if self.byr is None:
            return False
        if len(self.byr) != 4:
            return None
        int_byr = int(self.byr)
        if not (1920 <= int_byr <= 2002):
            return False
        return True

    def _is_iyr_valid(self):
        if self.iyr is None:
            return False
        if len(self.iyr) != 4:
            return None
        int_iyr = int(self.iyr)
        if not (2010 <= int_iyr <= 2020):
            return False
        return True

    def _is_eyr_valid(self):
        if self.eyr is None:
            return False
        if len(self.eyr) != 4:
            return None
        int_eyr = int(self.eyr)
        if not (2020 <= int_eyr <= 2030):
            return False
        return True

    def _is_hgt_valid(self):
        if self.hgt is None:
            return False
        if not self.hgt[:-2]:
            return False
        int_val = int(self.hgt[:-2])
        if 'cm' in self.hgt:
            if not (150 <= int_val <= 193):
                return False
        if 'in' in self.hgt:
            if not (59 <= int_val <= 76):
                return False
        return True

    def _is_hcl_valid(self):
        if self.hcl is None:
            return False
        hcl_regex = r"^(#([0-9]|[a-f]){6})+$"
        if re.match(hcl_regex, self.hcl):
            return True
        return False

    def _is_ecl_valid(self):
        if self.ecl is None:
            return False
        if self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
        return False

    def _is_pid_valid(self):
        if self.pid is None:
            return False
        if self.pid.isdigit() and len(self.pid) == 9:
            return True
        return False

    def __str__(self):
        return f"byr: {self.byr}"


def split_on_empty_lines(s):
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())


with open('input.txt', 'r') as file:
    content = file.read()
    after_split = split_on_empty_lines(content)
    valid_count = 0

    for line in after_split:
        passport_str = line.strip().replace('\n', ' ')
        passport = Passport(passport_str)
        if passport.is_valid():
            valid_count += 1
    print(valid_count)
