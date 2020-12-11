from typing import Dict

SeatingChart = Dict[complex, str]


def seating_io(_file_location):
    with open(_file_location, "r") as f:
        data = [list(line.strip()) for line in f.readlines()]
        return data


class SeatingSystem:
    adjacency = [
        complex(i, j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if not all([i == 0, j == 0])
    ]

    def __init__(self, seating_area):
        self.seating_area: SeatingChart = {}
        for i, row in enumerate(seating_area):
            for j, seat in enumerate(row):
                self.seating_area[complex(i, j)] = seat
        self.prior = None
        self.current = self.seating_area.copy()

    def __next__(self):
        self.prior = self.current.copy()
        self.current.clear()
        for seat in self.prior:
            self.current[seat] = self.next_seat_position(seat)

    def next_seat_position(self, seat):
        if self.prior[seat] == ".":
            return "."
        if self.prior[seat] == "#":
            n_occupied = 0
            for adj in self.adjacency:
                if self.prior.get(seat + adj, "L") == "#":
                    n_occupied += 1
            if n_occupied >= 4:
                return "L"
            else:
                return "#"
        if self.prior[seat] == "L":
            for adj in self.adjacency:
                if self.prior.get(seat + adj, "L") == "#":
                    return "L"
            return "#"

    def __str__(self):
        return str(self.current)

    def __eq__(self, other):
        return self.current == other

    def __repr__(self):
        return str(self)

    @property
    def occupied(self):
        return len([val for val in self.current.values() if val == "#"])

    @classmethod
    def from_file(cls, _file_location):
        with open(_file_location, "r") as f:
            data = [list(line.strip()) for line in f.readlines()]
            return cls(data)


def part_a(_file_location):
    ss = SeatingSystem.from_file(_file_location)
    while ss.prior != ss.current:
        next(ss)
    return ss.occupied


if __name__ == "__main__":
    file_location = "input.txt"
    print(part_a(file_location))
