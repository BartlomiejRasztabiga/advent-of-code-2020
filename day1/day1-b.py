with open('input.txt', 'r') as file:
    numbers = [int(x) for x in file.readlines()]
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if a + b + c == 2020:
                    print(a * b * c)